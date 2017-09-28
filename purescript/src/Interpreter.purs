module Interpreter (
    testNum,
    runInterpreter,
    environment,
    nextResume
) where


import Data.Argonaut.Core (jNull)
import Data.Functor ((<#>))
import Data.Map (lookup, fromFoldable)
import Data.Maybe (Maybe(..))
import Data.Traversable (traverse_)
import Data.Tuple (Tuple(..))
import Data.Tuple.Nested ((/\), over2, get1, get2)
import Data.Unfoldable (replicateA)
import Prelude ( Unit, bind, const, discard, pure, unit, when
               , (#), ($), (&&), (<<<), (==), (>>=), (||), (*>))
import Run (run)
import Run.Streaming (Resume(..), runYield, yield)
import Run.State (get, modify, evalState)
import Unsafe.Coerce (unsafeCoerce)


import Types ( AST(..), Statement(..), World, Definition(..), Interpreter
             , Expression(..), Direction, Move)
import World (step, moves, directions, facing)


testNum :: Int
testNum = 1


runInterpreter
  :: World
  -> AST
  -> Array (Tuple String Definition)
  -> Resume () Unit Unit World
runInterpreter initial (AST ss) baseDefs =
  run <<< runYield $
    evalState (fromFoldable baseDefs /\ initial /\ unit) $
      go (BlockStatement ss)
  where
    go :: Statement -> Interpreter
    go (CommandStatement command) = do
      defs <- get <#> get1
      case defs # lookup command of
        Just (Axiom a)       -> a
        Just (Procedure def) -> go $ BlockStatement def
        Nothing              -> pure unit -- This should be caught in verify.

    go (TimesStatement n child) = do
      _ :: Array Unit <- replicateA n $ go child
      pure unit

    go (IfStatement (BoolExp p) child) =
      when p $ go child

    go (BlockStatement childStatements) =
      childStatements # traverse_ go

    go (Comment _ _) =
      pure unit


send :: World -> Interpreter
send w = do
  yield w
  modify (over2 (const w))


sendMove :: Move -> Interpreter
sendMove m = do
  get <#> get2 <#> step m >>= send


nextResume
  :: forall a o. Resume () a Unit o
  -> {value :: o , resume :: Resume () a Unit o}
nextResume (Next o r') = {value: o, resume: run $ r' unit}
nextResume (Done _   ) = unsafeCoerce jNull


environment ::
  { turnLeft    :: Tuple String Definition
  , turnRight   :: Tuple String Definition
  , walkForward :: Tuple String Definition
  , moveLeft    :: Tuple String Definition
  , moveRight   :: Tuple String Definition
  , moveUp      :: Tuple String Definition
  , moveDown    :: Tuple String Definition
  }
environment = {

    turnLeft: Tuple "turnLeft" $
      Axiom (sendMove moves.turnLeft),

    turnRight: Tuple "turnRight" $
      Axiom (sendMove moves.turnRight),

    walkForward: Tuple "walkForward" $
      Axiom (sendMove moves.walkForward),

    moveLeft: Tuple "moveLeft" $
      Axiom (walk directions.left),

    moveRight: Tuple "moveRight" $
      Axiom (walk directions.right),

    moveUp: Tuple "moveUp" $
      Axiom (walk directions.up),

    moveDown: Tuple "moveDown" $
      Axiom (walk directions.down)

}


walk :: Direction -> Interpreter
walk dir = do
  adjustFacing
  sendMove moves.walkForward
  where
    adjustFacing :: Interpreter
    adjustFacing = do
      f <- get <#> get2 <#> facing
      case unit of
        _ | f == dir ->
            pure unit

          |  f == directions.up    && dir == directions.right
          || f == directions.down  && dir == directions.left
          || f == directions.left  && dir == directions.up
          || f == directions.right && dir == directions.down ->
            sendMove moves.turnRight

          | true -> do
            sendMove moves.turnLeft *> adjustFacing
    
