module Parser (
  parseAST,
  prettyPrint
) where


import Control.Alt ((<|>))
import Control.Lazy (defer)
import Control.Monad.State (State, evalState, get)
import Control.Monad.Trans.Class (lift)
import Data.Argonaut.Core (jNull)
import Data.Array (some, replicate, many, sortBy, head)
import Data.Either (Either(..))
import Data.Foldable (fold, any)
import Data.Int (fromString)
import Data.Maybe (Maybe(..), fromMaybe)
import Data.Ord (comparing)
import Data.Show (show)
import Data.String (fromCharArray, trim, toLower)
import Data.Tuple (Tuple, fst)
import Prelude ( (<$>), ($), (*>), (<*), (<>), (*), (+), (#), (/=), (==), (||)
               , (<*>), void, pure, bind, discard, map)
import Text.Parsing.Parser (ParserT, fail, runParserT)
import Text.Parsing.Parser.Combinators (try, between, optionMaybe, optional)
import Text.Parsing.Parser.String (string, skipSpaces, eof, satisfy, char)
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

import Levenshtein(editDistance)

-- Returns unsafe null to interact with javascript.
parseAST
  :: Array LanguageExtras
  -> Array (Tuple String Definition)
  -> String
  -> {ast :: AST, messages :: Array String, names :: Array String}
parseAST lang defs code =
  case evalState (runParserT code ast) (map fst defs) of
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

    go n (IfStatement p (BlockStatement ifs) Nothing) =
      fold [indentation n, "if (", showExp p, ") {", multi n ifs  , indentation n, "}"]

    go n (IfStatement p (BlockStatement ifs) (Just (BlockStatement elses))) =
      fold [indentation n, "if (", showExp p, ") {", multi n ifs  , indentation n,
                                         "} else {", multi n elses, indentation n, "}"]

    go n (IfStatement p s Nothing) =
      indentation n <> "if (" <> showExp p <> ")" <> go (n + 1) s

    go n (IfStatement p s (Just elses)) =
      indentation n <> "if (" <> showExp p <> ")" <> go (n + 1) s <> indentation n
                    <> "else {" <> go (n + 1) elses <> indentation n <> "}"

    go n (BlockStatement ss) =
      indentation n <> "{" <> multi n ss <> indentation n <> "}"

    go n (Comment true c) =
      indentation n <> "//" <> c

    go n (Comment false c) =
      " //" <> c

    showExp (BoolExp b) = show b
    showExp (Question ClearInFront) = "clearInFront?"


ast :: ParserT String (State (Array String)) AST
ast =
  AST <$> statements <* eof


statements :: ParserT String (State (Array String)) (Array Statement)
statements
  = many (defer $ \_ -> statement) <* skipSpaces


statement :: ParserT String (State (Array String)) Statement
statement
  = defer $ \_ -> try (keyword "times" *>
                        (TimesStatement
                         <$> parens positiveInt
                         <*> block))
              <|> try (keyword "if" *>
                        (IfStatement
                         <$> parens predicate
                         <*> block
                         <*> optionMaybe (try $ keyword "else" *> block)))
              <|> try blockStatement
              <|> try commandStatement
              <|> try comment


keyword :: String -> ParserT String (State (Array String)) String
keyword word = skipSpaces *> string word


parens :: forall a. ParserT String (State (Array String)) a -> ParserT String (State (Array String)) a
parens expression = do
  skipSpaces
  optional $ string "("
  skipSpaces
  ex <- expression
  skipSpaces
  optional $ string ")"
  pure ex


block :: ParserT String (State (Array String)) Statement
block = do
  st <- defer $ \_ -> statement
  pure $ case st of
    (BlockStatement _) -> st
    _                  -> BlockStatement [st]


blockStatement :: ParserT String (State (Array String)) Statement
blockStatement
  =  skipSpaces
  *> (BlockStatement <$> between (string "{") (string "}") (defer $ \_ -> statements))


commandStatement :: ParserT String (State (Array String)) Statement
commandStatement = do
  skipSpaces
  command <- some letter
  skipSpaces
  optional $ string ";"
  command' <- fixCommand (fromCharArray command) <$> lift get
  pure $ CommandStatement command'


fixCommand :: String -> Array String -> String
fixCommand c env = do
  env # sortBy (comparing editDist)
      # head
      # fromMaybe c
  where
    editDist x = editDistance (toLower x) (toLower c)


predicate :: ParserT String (State (Array String)) Expression
predicate = do
  expression <- fromCharArray <$> some (letter <|> char '?')
  case fixCommand expression ["true", "false", "clearInFront?", "clear"] of
    "true"          -> pure $ BoolExp  true        
    "false"         -> pure $ BoolExp  false       
    "clearInFront?" -> pure $ Question ClearInFront
    "clear"         -> pure $ Question ClearInFront
    _               -> fail $ expression <> " is not a predicate"


positiveInt :: ParserT String (State (Array String)) Int
positiveInt = do
  numbers <- fromCharArray <$> some digit
  case fromString numbers of
    Just n  -> pure n
    Nothing -> fail $ "Could not parse a positive int from: " <> numbers


newlineWhiteSpace :: ParserT String (State (Array String)) Boolean
newlineWhiteSpace = do
  ws <- many $ satisfy \c -> c == '\n' || c == '\r' || c == ' ' || c == '\t'
  pure $ any (\c -> c == '\n' || c == '\r') ws


comment :: ParserT String (State (Array String)) Statement
comment = do
  ownLine <- newlineWhiteSpace
  void $ string "//"
  c <- some $ satisfy \c -> c /= '\n'
  pure $ Comment ownLine (fromCharArray c)
