module World (
    moves,
    directions,
    step,
    facing,
    predicates,
    inspect
) where

import Types (World, Move, Direction, RobotPredicate)

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
foreign import predicates ::
  { clearInFront :: RobotPredicate
  }
foreign import step :: Move -> World -> World
foreign import facing :: World -> Direction
foreign import inspect :: RobotPredicate -> World -> Boolean
