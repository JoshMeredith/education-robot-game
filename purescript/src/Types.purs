module Types (
    AST(..),
    Statement(..),
    Expression(..),
    LanguageExtras(..),
    Definition(..),
    World,
    Move,
    Direction,
    Interpreter
) where


import Data.Eq (class Eq, (==))
import Data.Map (Map)
import Data.Tuple.Nested (type (/\))
import Prelude (Unit)
import Run (Run)
import Run.Streaming (YIELD)
import Run.State (STATE)
import Unsafe.Coerce (unsafeCoerce)


foreign import data World     :: Type
foreign import data Move      :: Type
foreign import data Direction :: Type


data AST
   = AST (Array Statement)


data Statement
   = CommandStatement String
   | TimesStatement Int        Statement
   | IfStatement    Expression Statement
   | BlockStatement (Array Statement)
   | Comment        Boolean String


data Expression
   = BoolExp Boolean


data LanguageExtras
   = TimesLoop
   | IfBranching


type Interpreter
   = Run ( yield :: YIELD World
         , state :: STATE (Map String Definition /\ World /\ Unit)
         )
         Unit


data Definition
   = Procedure (Array Statement)
   | Axiom Interpreter


instance eqMove :: Eq Move where
  eq x y = (unsafeCoerce x :: Int) == (unsafeCoerce y :: Int)


instance eqDirection :: Eq Direction where
  eq x y = (unsafeCoerce x :: Int) == (unsafeCoerce y :: Int)
