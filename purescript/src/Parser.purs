module Parser (
  parseAST,
  prettyPrint
) where


import Control.Alt ((<|>))
import Control.Lazy (defer)
import Data.Argonaut.Core (jNull)
import Data.Array (some, replicate, many)
import Data.Either (Either(..))
import Data.Foldable (fold)
import Data.Int (fromString)
import Data.Map (Map)
import Data.Maybe (Maybe(..))
import Data.Show (show)
import Data.String (fromCharArray)
import Prelude ( (<$>), ($), (*>), (<*), (<>), (*), (+), (#), (/=), (==), (||)
               , (<<<), void, pure, bind, discard, map)
import Text.Parsing.Parser (Parser, fail, runParser)
import Text.Parsing.Parser.Combinators (try, between)
import Text.Parsing.Parser.String (string, skipSpaces, eof, char, satisfy)
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

    go n (IfStatement (BoolExp p) (BlockStatement ss)) =
      fold [indentation n, "if (", show p, ") {", multi n ss, "}"]

    go n (IfStatement (BoolExp p) s) =
      indentation n <> "if (" <> show p <> ")" <> go (n + 1) s

    go n (BlockStatement ss) =
      indentation n <> "{" <> multi n ss <> "}"

    go n (Comment true c) =
      indentation n <> "//" <> c

    go n (Comment false c) =
      " //" <> c


ast :: Parser String AST
ast =
  AST <$> statements <* eof


statements :: Parser String (Array Statement)
statements
  -- = fromFoldable <$> (skipSpaces *> sepEndBy (defer $ \_ -> statement) skipSpaces)
  = many (defer $ \_ -> statement) <* skipSpaces


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
  skipSpaces
  void $ string keyword
  skipSpaces
  void $ string "("
  skipSpaces
  count <- expression
  skipSpaces
  void $ string ")"
  skipSpaces
  subStatement <- blockStatement
  pure $ constructor count subStatement


blockStatement :: Parser String Statement
blockStatement
  =  skipSpaces
  *> (BlockStatement <$> between (string "{") (string "}") (defer $ \_ -> statements))


commandStatement :: Parser String Statement
commandStatement = do
  skipSpaces
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


newlineWhiteSpace :: Parser String Boolean
newlineWhiteSpace = try whitespaceWithoutNewline 
                <|>     whitespaceWithNewline
  where
    whitespaceWithoutNewline = do
      void <<< many $ satisfy \c -> c == ' ' || c == '\t'
      pure false

    whitespaceWithNewline = do
      void <<< some $ satisfy \c -> c == '\n' || c == '\r' || c == ' ' || c == '\t'
      pure true


comment :: Parser String Statement
comment = do
  ownLine <- newlineWhiteSpace
  void $ string "//"
  c <- some $ satisfy \c -> c /= '\n'
  void $ char '\n'
  pure $ Comment ownLine ("//" <> fromCharArray c)
