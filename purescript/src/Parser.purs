module Parser (
  parseAST,
  prettyPrint
) where


import Control.Alt ((<|>))
import Control.Lazy (defer)
import Control.Monad.State.Class (get)
import Data.Argonaut.Core (jNull)
import Data.Array (some, fromFoldable, replicate)
import Data.Either (Either(..))
import Data.Foldable (fold)
import Data.Int (fromString)
import Data.Map (Map)
import Data.Maybe (Maybe(..))
import Data.Show (show)
import Data.String (fromCharArray)
import Prelude ( (<$>), ($), (*>), (<*), (<>), (*), (+), (#)
               , void, pure, bind, discard, map, (==))
import Text.Parsing.Parser (Parser, fail, runParser, ParseState(..))
import Text.Parsing.Parser.Combinators (try, sepEndBy, between)
import Text.Parsing.Parser.Pos (Position(..))
import Text.Parsing.Parser.String (string, skipSpaces, eof, noneOf, char)
import Text.Parsing.Parser.Token (letter, digit)
import Unsafe.Coerce (unsafeCoerce)


import Types(
  AST(..),
  Statement(..),
  Expression(..),
  LanguageExtras,
  Definition,
  Primitive(..)
)


-- Returns unsafe null to interact with javascript.
parseAST
  :: Array LanguageExtras
  -> Map String Definition
  -> String
  -> {ast :: AST, messages :: Array String, names :: Array String}
parseAST lang defs code =
  case runParser code ast of
    Left  _ -> {ast: unsafeCoerce jNull, messages: [], names: []}
    Right a -> {ast: a                 , messages: [], names: []}


prettyPrint :: AST -> String
prettyPrint (AST a) = a # map (go 0) # fold
  where
    tabWidth = 4
    indentation n = "\n" <> (fold $ replicate (tabWidth * n) " ")
    multi n ss = fold (map (go $ n + 1) ss)

    go n (CommandStatement s) =
      indentation n <> s <> ";"

    go n (TimesStatement t (BlockStatement ss)) =
      fold [indentation n, "times (", show t, ") {", multi n ss, "}"]

    go n (TimesStatement t s) =
      indentation n <> "times (" <> show t <> ")" <> go (n + 1) s

    go n (IfStatement p (BlockStatement ss)) =
      fold [indentation n, "if (", "IMPLEMENT BRANCHING", ") {", multi n ss, "}"]

    go n (IfStatement p s) =
      indentation n <> "if (" <> "IMPLEMENT BRANCHING" <> ")" <> go (n + 1) s

    go n (BlockStatement ss) =
      indentation n <> "{" <> multi n ss <> "}"

    go n (PrimitiveStatement TurnLeft) =
      indentation n <> "{[TurnLeft]}"
    go n (PrimitiveStatement TurnRight) =
      indentation n <> "{[TurnRight]}"
    go n (PrimitiveStatement WalkForward) =
      indentation n <> "{[WalkForward]}"



ast :: Parser String AST
ast =
  AST <$> statements <* eof


statements :: Parser String (Array Statement)
statements
  = fromFoldable <$> (skipSpaces *> sepEndBy (defer $ \_ -> statement) skipSpaces)


statement :: Parser String Statement
statement
  = defer $ \_ -> try (structuredStatement "times" TimesStatement positiveInt)
              <|> try (structuredStatement "if"    IfStatement    trueFalse  )
              <|> try blockStatement
              <|> try commandStatement
              <|> try comment


structuredStatement
  :: forall a.
     String
  -> (a -> Statement -> Statement)
  -> Parser String a
  -> Parser String Statement
structuredStatement keyword constructor expression = do
  void $ string keyword
  skipSpaces
  void $ string "("
  skipSpaces
  count <- expression
  skipSpaces
  void $ string ")"
  skipSpaces
  subStatement <- statement -- defer $ \_ -> statement
  pure $ constructor count subStatement


blockStatement :: Parser String Statement
blockStatement
  = BlockStatement <$> between (string "{") (string "}") (defer $ \_ -> statements)


commandStatement :: Parser String Statement
commandStatement = do
  command <- some letter
  skipSpaces
  void $ string ";"
  pure $ CommandStatement (fromCharArray command)


trueFalse :: Parser String Expression
trueFalse = try (string "true"  *> pure (BoolExp true ))
        <|>     (string "false" *> pure (BoolExp false))


positiveInt :: Parser String Int
positiveInt = do
  numbers <- fromCharArray <$> some digit
  case fromString numbers of
    Just n  -> pure n
    Nothing -> fail $ "Could not parse a positive int from: " <> numbers


lineStart :: Parser String Boolean
lineStart = do
  (ParseState _ (Position {column: col}) _) <- get
  pure (col == 1)


comment :: Parser String Statement
comment = do
  ownLine <- lineStart
  skipSpaces
  void $ string "//"
  c <- some $ noneOf ['\n']
  void $ char '\n'
  pure $ Comment ownLine ("//" <> fromCharArray c)
