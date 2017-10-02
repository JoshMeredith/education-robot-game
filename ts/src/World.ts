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
    // TODO(junkbot): Actually store Grid (e.g. objects in each cell), etc.

    constructor(readonly rows: number, readonly cols: number, readonly goal: Coord2D,
        readonly playerLocation: Coord2D, readonly facing: Direction,
        readonly hasFailed = false) {}

    public playerFacing(): Direction {
        return this.facing;
    }

    public failed(): boolean {
        return this.hasFailed;
    }

    public victory(): boolean {
        return (this.playerLocation.row == this.goal.row &&
            this.playerLocation.col == this.goal.col);
    }

    public static test(): number {
        return Purescript.Interpreter.testNum;
    }

    public step(move: PlayerAction): Grid {
        // Need to consider order of operations with this:
        // I think the ideal order is move all time varying obstacles one
        // tick, and complete the player move, THEN check for validity.
        // That way, for example, a player would be able to step over a
        // spike pit that toggles on and off for one tick.
        
        let newDir = this.facing;
        let newRow = this.playerLocation.row;
        let newCol = this.playerLocation.col;
        let newFailure = this.hasFailed;

        switch (move) {
            case PlayerAction.TurnLeft: {
                newDir = (this.facing + 1) % 4;
                break;
            }
            case PlayerAction.TurnRight: {
                newDir = (this.facing + 3) % 4;
                break;
            }
            case PlayerAction.WalkForward: {
                const dRow = [-1, 0, 1, 0];
                const dCol = [0, -1, 0, 1];

                let tmpRow = this.playerLocation.row + dRow[newDir];
                let tmpCol = this.playerLocation.col + dCol[newDir];

                if (!(newRow >= 0 && newCol >= 0 &&
                    newRow < this.rows && newCol < this.cols)) {
                    newFailure = true;
                } else {
                    newRow = tmpRow;
                    newCol = tmpCol;
                }
                break;
            }
        }

        return new Grid(
            this.rows,
            this.cols,
            this.goal,
            new Coord2D(newRow, newCol),
            newDir,
            newFailure);
    }

    public render(sprites: Sprites): string[][][] {
        var grid: string[][][] = [];

        for (var y = 0; y < this.rows; y++) {
            grid[y] = [];
            for (var x = 0; x < this.cols; x++) {
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
