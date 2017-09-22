module Types (
    AST(..),
    Statement(..),
    Expression(..),
    Primitive(..),
    LanguageExtras(..),
    Definition(..)
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


data LanguageExtras
   = TimesLoop
   | IfBranching


data Definition
   = Procedure (Array Statement)
