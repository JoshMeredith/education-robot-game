module World (
    moves,
    directions,
    step,
    facing
) where

import Types (World, Move, Direction)

foreign import moves ::
  { turnLeft    :: Move
  , turnRight   :: Move
  , walkForward :: Move
  }
foreign import directions :: 
  { up    :: Direction
  , down  :: Direction
  , left  :: Direction
  , right :: Direction
  }
foreign import unsafeStep :: Move -> World -> World
foreign import facing :: World -> Direction
foreign import isNull :: World -> Boolean


step :: Move -> World -> World
step m w =
  case unsafeStep m w of
    w' | isNull w' -> w
       | true      -> w'
