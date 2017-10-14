module Parser (
  parseAST,
  prettyPrint
) where


import Control.Alt ((<|>))
import Control.Lazy (defer)
import Data.Argonaut.Core (jNull)
import Data.Array (some, replicate, many)
import Data.Either (Either(..))
import Data.Foldable (fold, any)
import Data.Int (fromString)
import Data.Maybe (Maybe(..))
import Data.Show (show)
import Data.String (fromCharArray, trim)
import Data.Tuple (Tuple)
import Prelude ( (<$>), ($), (*>), (<*), (<>), (*), (+), (#), (/=), (==), (||)
               , (<*>), void, pure, bind, discard, map)
import Text.Parsing.Parser (Parser, fail, runParser)
import Text.Parsing.Parser.Combinators (try, between, optionMaybe)
import Text.Parsing.Parser.String (string, skipSpaces, eof, satisfy)
import Text.Parsing.Parser.Token (letter, digit)
import Unsafe.Coerce (unsafeCoerce)


import Types(
  AST(..),
  Statement(..),
  Expression(..),
  LanguageExtras,
  Definition,
  Questions(..)
)


-- Returns unsafe null to interact with javascript.
parseAST
  :: Array LanguageExtras
  -> Array (Tuple String Definition)
  -> String
  -> {ast :: AST, messages :: Array String, names :: Array String}
parseAST lang defs code =
  case runParser code ast of
    Left  _ -> {ast: unsafeCoerce jNull, messages: [], names: []}
    Right a -> {ast: a                 , messages: [], names: []}


prettyPrint :: AST -> String
prettyPrint (AST a) = a # map (go 0) # fold # trim
  where
    tabWidth = 4
    indentation n = "\n" <> (fold $ replicate (tabWidth * n) " ")
    multi n ss = fold (map (go $ n + 1) ss)

    go n (CommandStatement s) =
      indentation n <> s <> ";"

    go n (TimesStatement t (BlockStatement ss)) =
      fold [indentation n, "times (", show t, ") {", multi n ss, indentation n, "}"]

    go n (TimesStatement t s) =
      indentation n <> "times (" <> show t <> ")" <> go (n + 1) s

    go n (IfStatement p (BlockStatement ss)) =
      fold [indentation n, "if (", showExp p, ") {", multi n ss, indentation n, "}"]

    go n (IfStatement p s) =
      indentation n <> "if (" <> showExp p <> ")" <> go (n + 1) s

    go n (BlockStatement ss) =
      indentation n <> "{" <> multi n ss <> indentation n <> "}"

    go n (Comment true c) =
      indentation n <> "//" <> c

    go n (Comment false c) =
      " //" <> c

    showExp (BoolExp b) = show b
    showExp (Question ClearInFront) = "clearInFront?"


ast :: Parser String AST
ast =
  AST <$> statements <* eof


statements :: Parser String (Array Statement)
statements
  = many (defer $ \_ -> statement) <* skipSpaces


statement :: Parser String Statement
statement
  = defer $ \_ -> try (keyword "times" *>
                        (TimesStatement
                         <$> parens positiveInt
                         <*> blockStatement))
              <|> try (keyword "if" *>
                        (IfStatement
                         <$> parens predicate
                         <*> blockStatement))
              <|> try blockStatement
              <|> try commandStatement
              <|> try comment


keyword :: String -> Parser String String
keyword word = skipSpaces *> string word


parens :: forall a. Parser String a -> Parser String a
parens expression = do
  skipSpaces
  between (string "(") (string ")") expression


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


predicate :: Parser String Expression
predicate = try (string "true"          *> pure (BoolExp  true        ))
        <|> try (string "false"         *> pure (BoolExp  false       ))
        <|>     (string "clearInFront?" *> pure (Question ClearInFront))


positiveInt :: Parser String Int
positiveInt = do
  numbers <- fromCharArray <$> some digit
  case fromString numbers of
    Just n  -> pure n
    Nothing -> fail $ "Could not parse a positive int from: " <> numbers


newlineWhiteSpace :: Parser String Boolean
newlineWhiteSpace = do
  ws <- many $ satisfy \c -> c == '\n' || c == '\r' || c == ' ' || c == '\t'
  pure $ any (\c -> c == '\n' || c == '\r') ws


comment :: Parser String Statement
comment = do
  ownLine <- newlineWhiteSpace
  void $ string "//"
  c <- some $ satisfy \c -> c /= '\n'
  pure $ Comment ownLine (fromCharArray c)
