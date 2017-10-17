module Levenshtein (
    editDistance
) where

foreign import editDistance :: String -> String -> Int
