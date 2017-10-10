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

export enum Ground {
    Clear,
    Wall
}

export class Obstacle {
    constructor( readonly type: Ground
               , readonly sprites: string[]
               ) {}
}

export class Coord2D {
    constructor(readonly row: number, readonly col: number) {}
}

export class Grid {
    constructor(readonly rows: number, readonly cols: number,
        readonly sprites: Sprites, readonly goal: Coord2D,
        readonly playerLocation: Coord2D, readonly facing: Direction,
        private world: Obstacle[][] = [], readonly hasFailed = false) {

        // Assume the grid is always initialised properly, if it is.
        if (world.length != rows) {
            for (var y = 0; y < this.rows; y++) {
                this.world[y] = [];
                for (var x = 0; x < this.cols; x++) {
                    this.world[y][x] = new Obstacle(Ground.Clear, [this.sprites.grass]);
                }
            }
        }
    }

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
        return PS.Interpreter.testNum;
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

                let nextBlock = Ground.Wall;
                if (tmpRow >= 0 && tmpCol >= 0 &&
                    tmpRow < this.rows && tmpCol < this.cols) {
                    nextBlock = this.world[tmpRow][tmpCol].type;
                }

                switch (nextBlock) {
                    case (Ground.Clear): {
                        newRow = tmpRow;
                        newCol = tmpCol;
                        break;
                    }
                    case (Ground.Wall): { // Do nothing.
                        break;
                    }
                }
                break;
            }
        }

        return new Grid(
            this.rows,
            this.cols,
            this.sprites,
            this.goal,
            new Coord2D(newRow, newCol),
            newDir,
            this.world,
            newFailure
        );
    }

    public render(): string[][][] {
        var grid: string[][][] = [];

        let render_rows = this.rows + 2;
        let render_cols = this.cols + 2;

        for (var y = 0; y < render_rows; y++) {
            grid[y] = [];
            for (var x = 0; x < render_cols; x++) {
                grid[y][x] = [this.sprites.ground];
                if (y >= 1 && x >= 1 &&
                    y < render_rows - 1 && x < render_cols - 1) {
                    grid[y][x] = [...grid[y][x], ...this.world[y - 1][x - 1].sprites];
                }
            }
        }

        // Add walls.
        for (var x = 1; x < render_cols - 1; x++) {
            grid[0          ][x].push(this.sprites.wall.horizontal);
            grid[this.rows+1][x].push(this.sprites.wall.horizontal);
        }
        for (var y = 1; y < render_rows - 1; y++) {
            grid[y][0          ].push(this.sprites.wall.vertical);
            grid[y][this.cols+1].push(this.sprites.wall.vertical);
        }
        grid[0              ][0              ].push(this.sprites.wall.topLeft);
        grid[0              ][render_cols - 1].push(this.sprites.wall.topRight);
        grid[render_rows - 1][0              ].push(this.sprites.wall.bottomLeft);
        grid[render_rows - 1][render_cols - 1].push(this.sprites.wall.bottomRight);

        grid[this.goal.row + 1][this.goal.col + 1].push(this.sprites.goal);

        grid[this.playerLocation.row + 1]
            [this.playerLocation.col + 1]
            .push(this.sprites.player[Direction[this.facing]]);

        return grid;
    }
}

interface Sprites {
    ground: string,
    grass: string,
    player: {
        Up: string,
        Down: string,
        Left: string,
        Right: string
    },
    goal: string,
    wall: {
        horizontal: string,
        vertical: string,
        topLeft: string,
        topRight: string,
        bottomLeft: string,
        bottomRight: string
    }
}

}
