module Types (
    AST(..),
    Statement(..),
    Expression(..),
    Primitive(..),
    LanguageExtras(..),
    Definition(..),
    World,
    Move,
    Direction
) where


foreign import data World     :: Type
foreign import data Move      :: Type
foreign import data Direction :: Type


data AST
   = AST (Array Statement)


data Statement
   = CommandStatement String
   | TimesStatement Expression Statement
   | IfStatement    Expression Statement
   | BlockStatement (Array Statement)
   | PrimitiveStatement Primitive


data Expression
   = IntExp Int


data Primitive
   = TurnLeft
   | TurnRight
   | WalkForward


data LanguageExtras
   = TimesLoop
   | IfBranching


data Definition
   = Procedure (Array Statement)
