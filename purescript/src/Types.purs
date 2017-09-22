module Types (
    AST(..),
    Statement(..),
    Expression(..),
    Primitive(..)
) where


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
