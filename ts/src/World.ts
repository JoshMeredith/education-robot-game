namespace World {

export enum Direction {
    // Explicitly numbered for directional purposes.
    Up = 0,
    Left = 1,
    Down = 2,
    Right = 3
}

export enum PlayerAction {
    TurnLeft,
    TurnRight,
    WalkForward
}

export class Coord2D {
    constructor(readonly row: number, readonly col: number) {}
}

export class Grid {
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

    public playerFacing(): Direction {
        return this.facing;
    }

    public victory(): boolean {
        return (this.playerLocation.row == this.goal.row &&
            this.playerLocation.col == this.goal.col);
    }

    public static test(): number {
        return Purescript.Interpreter.testNum;
    }

    public step(move: PlayerAction): Grid | null {
        // Need to consider order of operations with this:
        // I think the ideal order is move all time varying obstacles one
        // tick, and complete the player move, THEN check for validity.
        // That way, for example, a player would be able to step over a
        // spike pit that toggles on and off for one tick.
        
        // Adjust the direction the player is facing.
        let newDir = this.facing;
        var newRow = this.playerLocation.row;
        var newCol = this.playerLocation.col;
        if (move == PlayerAction.TurnLeft) {
            newDir = (this.facing + 1)%4;
        } else if (move == PlayerAction.TurnRight) {
            newDir = (this.facing + 3)%4;
        } else if (move == PlayerAction.WalkForward) {
            const dRow = [-1, 0, 1, 0];
            const dCol = [0, -1, 0, 1];
            newRow += dRow[newDir];
            newCol += dCol[newDir];

            if (!(newRow >= 0 && newCol >= 0 &&
                newRow < this.numRows && newCol < this.numCols)) {
                return null;
            }
        }

        return new Grid( this.numRows
                       , this.numCols
                       , this.goal
                       , new Coord2D(newRow, newCol)
                       , newDir
                       );
    }

    public render(sprites: Sprites): string[][][] {
        var grid: string[][][] = [];

        for (var y = 0; y < this.numRows; y++) {
            grid[y] = [];
            for (var x = 0; x < this.numCols; x++) {
                grid[y][x] = [];
                grid[y][x].push(sprites.grass());
            }
        }

        grid[this.playerLocation.row]
            [this.playerLocation.col]
            .push(sprites.player[Direction[this.facing]]);

        grid[this.goal.row][this.goal.col].push(sprites.goal);

        return grid;
    }
}

interface Sprites {
    grass(): string,
    player: {
        Up: string,
        Down: string,
        Left: string,
        Right: string
    },
    goal: string
}

}
