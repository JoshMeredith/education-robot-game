module Parser (
  parseAST
) where


import Control.Alt ((<|>))
import Control.Lazy (defer)
import Data.Argonaut.Core (jNull)
import Data.Array (some, fromFoldable)
import Data.Either (Either(..))
import Data.Int (fromString)
import Data.Map (Map)
import Data.Maybe (Maybe(..))
import Data.String (fromCharArray)
import Prelude ((<$>), ($), (*>), (<*), (<>), void, pure, bind, discard)
import Text.Parsing.Parser (Parser, fail, runParser)
import Text.Parsing.Parser.Combinators (try, sepEndBy, between)
import Text.Parsing.Parser.String (string, skipSpaces, eof)
import Text.Parsing.Parser.Token (letter, digit)
import Unsafe.Coerce (unsafeCoerce)


import Types(
  AST(..),
  Statement(..),
  Expression(..),
  LanguageExtras,
  Definition
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
