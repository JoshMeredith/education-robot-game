module Parser where


import Control.Alt ((<|>))
import Control.Lazy (defer)
import Data.Array (some, fromFoldable)
import Data.Int (fromString)
import Data.Maybe (Maybe(..))
import Data.String (fromCharArray)
import Prelude((<$>), ($), (*>), (<*), (<>), void, pure, bind, discard)
import Text.Parsing.Parser(Parser, fail)
import Text.Parsing.Parser.Combinators (try, sepEndBy, between)
import Text.Parsing.Parser.String (string, skipSpaces, eof)
import Text.Parsing.Parser.Token (letter, digit)


import Types(AST(..), Statement(..), Expression(..))


ast :: Parser String AST
ast =
  AST <$> statements <* eof


statements :: Parser String (Array Statement)
statements
  = fromFoldable <$> (skipSpaces *> sepEndBy (defer $ \_ -> statement) skipSpaces)


statement :: Parser String Statement
statement
  = defer $ \_ -> try (structuredStatement "times" TimesStatement)
              <|> try (structuredStatement "if"    IfStatement   )
              <|> try blockStatement
              <|> try commandStatement


structuredStatement
  :: String
  -> (Expression -> Statement -> Statement)
  -> Parser String Statement
structuredStatement keyword constructor = do
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


expression :: Parser String Expression
expression =
  IntExp <$> positiveInt


positiveInt :: Parser String Int
positiveInt = do
  numbers <- fromCharArray <$> some digit
  case fromString numbers of
    Just n  -> pure n
    Nothing -> fail $ "Could not parse a positive int from: " <> numbers
