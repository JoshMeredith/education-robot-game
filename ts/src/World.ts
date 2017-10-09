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
    private world: Obstacle[][] = [];
    readonly rows: number;
    readonly cols: number;

    constructor(interior_height: number, interior_width: number,
        readonly sprites: Sprites, readonly goal: Coord2D,
        readonly playerLocation: Coord2D, readonly facing: Direction,
        readonly hasFailed = false)
    {
        this.rows = interior_height + 2;
        this.cols = interior_width  + 2;
        this.world[0] = [];
        this.world[this.rows-1] = [];
        for (var y = 1; y < this.rows - 1; y++) {
            this.world[y] = [];
            for (var x = 1; x < this.cols - 1; x++) {
                this.world[y][x] = new Obstacle(Ground.Clear, [this.sprites.grass]);
            }
        }
        for (var x = 1; x < this.cols - 1; x++) {
            this.world[0          ][x] = new Obstacle(Ground.Wall, [this.sprites.wall.horizontal]);
            this.world[this.rows-1][x] = new Obstacle(Ground.Wall, [this.sprites.wall.horizontal]);
        }
        for (var y = 1; y < this.rows - 1; y++) {
            this.world[y][0          ] = new Obstacle(Ground.Wall, [this.sprites.wall.vertical]);
            this.world[y][this.cols-1] = new Obstacle(Ground.Wall, [this.sprites.wall.vertical]);
        }
        this.world[0          ][0          ] = new Obstacle(Ground.Wall, [this.sprites.wall.topLeft]);
        this.world[0          ][this.cols-1] = new Obstacle(Ground.Wall, [this.sprites.wall.topRight]);
        this.world[this.rows-1][0          ] = new Obstacle(Ground.Wall, [this.sprites.wall.bottomLeft]);
        this.world[this.rows-1][this.cols-1] = new Obstacle(Ground.Wall, [this.sprites.wall.bottomRight]);
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

                switch (this.world[tmpRow][tmpCol].type) {
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
            this.rows - 2,
            this.cols - 2,
            this.sprites,
            this.goal,
            new Coord2D(newRow, newCol),
            newDir,
            newFailure);
    }

    public render(): string[][][] {
        var grid: string[][][] = [];

        for (var y = 0; y < this.rows; y++) {
            grid[y] = [];
            for (var x = 0; x < this.cols; x++) {
                grid[y][x] = [this.sprites.ground];
                Array.prototype.push.apply(grid[y][x], this.world[y][x].sprites);
            }
        }

        grid[this.goal.row][this.goal.col].push(this.sprites.goal);

        grid[this.playerLocation.row]
            [this.playerLocation.col]
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
