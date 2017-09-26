module Interpreter (
    testNum,
    runInterpreter,
    environment
) where


import Data.Argonaut.Core (jNull)
import Data.Functor ((<#>))
import Data.Map (Map, lookup)
import Data.Maybe (Maybe(..))
import Data.Set (Set)
import Data.Set (fromFoldable) as Set
import Data.Traversable (traverse_)
import Data.Tuple
import Data.Tuple.Nested ((/\), type (/\), over2, get1, get2)
import Data.Unfoldable (replicateA)
import Prelude ( Unit, bind, discard, pure, void, ($), unit, when, (<<<)
               , (<$>), (*>), (<*), (<>), (<), (-), (#), (>>=), const
               , (==), (||), (&&))
import Run (Run, run)
import Run.Streaming (Resume(..), runYield, yield, YIELD)
import Run.State (STATE, get, modify, evalState)
import Unsafe.Coerce (unsafeCoerce)


import Types ( AST(..), Statement(..), World, Definition(..), Interpreter
             , Expression(..), Primitive(..), Direction)
import World (step, moves, directions, facing)


testNum :: Int
testNum = 1


runInterpreter
  :: World
  -> AST
  -> Map String Definition
  -> Resume () Unit Unit World
runInterpreter initial (AST ss) baseDefs =
  run <<< runYield $
    evalState (baseDefs /\ initial /\ unit) $ go (BlockStatement ss)
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

    go (PrimitiveStatement prim) = do
      get <#> get2 <#> step (move prim) >>= send

    move TurnLeft    = moves.turnLeft
    move TurnRight   = moves.turnRight
    move WalkForward = moves.walkForward


send :: World -> Interpreter
send w = do
  yield w
  modify (over2 (const w))


nextResume
  :: forall r a o. Resume r a Unit o
  -> {value :: o , resume :: Run r (Resume r a Unit o)}
nextResume (Next o r') = {value: o, resume: r' unit}
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
      Procedure [PrimitiveStatement TurnLeft],

    turnRight: Tuple "turnRight" $
      Procedure [PrimitiveStatement TurnRight],

    walkForward: Tuple "walkForward" $
      Procedure [PrimitiveStatement WalkForward],

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
  get <#> get2 <#> step moves.walkForward >>= send
  where
    adjustFacing :: Interpreter
    adjustFacing = do
      w <- get <#> get2 
      let f = w # facing
      case unit of
        _ | f == dir ->
            pure unit

          |  f == directions.up    && dir == directions.right
          || f == directions.down  && dir == directions.left
          || f == directions.left  && dir == directions.up
          || f == directions.right && dir == directions.down ->
            w # step moves.turnRight # send

          | true -> do
            w # step moves.turnLeft # send
            adjustFacing
    
