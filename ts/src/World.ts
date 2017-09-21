enum Direction {
    // Explicitly numbered for directional purposes.
    Up = 0,
    Left = 1,
    Down = 2,
    Right = 3
}

enum PlayerAction {
    TurnLeft,
    TurnRight,
    WalkForward
}

class Coord2D {
    row: number;
    col: number;
}

class World {
    readonly numRows: number;
    readonly numCols: number;

    readonly playerLocation: Coord2D;
    readonly facing: Direction;

    readonly goal: Coord2D;

    // TODO(junkbot): World grid, etc.

    constructor(rows: number, cols: number, goal: Coord2D, playerAt: Coord2D,
        playerDir: Direction) {
        this.numRows = rows;
        this.numCols = cols;
        this.playerLocation = playerAt;
        this.facing = playerDir;
        this.goal = goal;
    }

    get playerFacing(): Direction {
        return this.facing;
    }

    public victory(): boolean {
        return (this.playerLocation.row == this.goal.row &&
            this.playerLocation.col == this.goal.col);
    }

    public static test(): number {
        return Purescript.Interpreter.testNum;
    }

    public step(move: PlayerAction): World | null {
        // Need to consider order of operations with this:
        // I think the ideal order is move all time varying obstacles one
        // tick, and complete the player move, THEN check for validity.
        // That way, for example, a player would be able to step over a
        // spike pit that toggles on and off for one tick.
        
        // Adjust the direction the player is facing.
        let newDir = this.facing;
        let newLocation = this.playerLocation;
        if (move == PlayerAction.TurnLeft) {
            newDir = (this.facing + 1)%4;
        } else if (move == PlayerAction.TurnRight) {
            newDir = (this.facing + 3)%4;
        } else if (move == PlayerAction.WalkForward) {
            const dRow = [-1, 0, 1, 0];
            const dCol = [0, -1, 0, 1];
            newLocation.row += dRow[newDir];
            newLocation.col += dCol[newDir];

            if (!(newLocation.row >= 0 && newLocation.col >= 0 &&
                newLocation.row < this.numRows && newLocation.col < this.numCols)) {
                return null;
            }
        }

        return new World(this.numRows, this.numCols, this.goal, newLocation, newDir);
    }
}
