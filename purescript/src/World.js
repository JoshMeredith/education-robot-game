"use strict";

exports.directions = {
    up:    World.Direction.Up,
    down:  World.Direction.Down,
    left:  World.Direction.Left,
    right: World.Direction.Right
}

exports.moves = {
    turnLeft:    World.PlayerAction.TurnLeft,
    turnRight:   World.PlayerAction.TurnRight,
    walkForward: World.PlayerAction.WalkForward
}

exports.predicates = {
    clearInFront: World.RobotPredicate.ClearInFront
}

exports.facing = function(world) {
    return world.playerFacing();
}

exports.step = function(move) {
    return function(world) {
        return world.step(move);
    }
}

exports.inspect = function(predicate) {
    return function(world) {
        return world.inspect(predicate);
    }
}
