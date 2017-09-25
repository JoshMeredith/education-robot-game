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
foreign import step :: Move -> World -> World
foreign import facing :: World -> Direction
