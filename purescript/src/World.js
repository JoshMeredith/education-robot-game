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

exports.facing = function(world) {
    return world.playerFacing();
}

exports.unsafeStep = function(move) {
    return function(world) {
        return world.step(move);
    }
}

exports.isNull = function(world) {
    return world === null;
}
