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

export enum RobotPredicate {
    ClearInFront
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

    public nextLocation(dir: Direction): Coord2D {
        const dRow = [-1, 0, 1, 0];
        const dCol = [0, -1, 0, 1];

        return new Coord2D(this.row + dRow[dir], this.col + dCol[dir])
    }
}

export function shorthandGrid(grid: string[][], sprites: Sprites): Obstacle[][] {
    var out: Obstacle[][] = [];

    for (var y = 0; y < grid.length; y++) {
        out[y] = [];
        for (var x = 0; x < grid[y].length; x++) {
            out[y][x] = obstacleFromShorthand(grid[y][x], sprites);
        }
    }

    return out;
}

function obstacleFromShorthand(sh: string, sprites: Sprites): Obstacle {
    switch (sh) {
        case '_': {
            return new Obstacle(Ground.Clear, [sprites.grass]);
        }
        case 'V': {
            return new Obstacle(Ground.Wall, [sprites.wall.full]);
        }
        case 'H': {
            return new Obstacle(Ground.Wall, [sprites.wall.full]);
        }
        case 'TL': {
            return new Obstacle(Ground.Wall, [sprites.wall.full]);
        }
        case 'TR': {
            return new Obstacle(Ground.Wall, [sprites.wall.full]);
        }
        case 'BL': {
            return new Obstacle(Ground.Wall, [sprites.wall.full]);
        }
        case 'BR': {
            return new Obstacle(Ground.Wall, [sprites.wall.full]);
        }
    }
}

export class Grid {
    public static init(
        rows: number,
        cols: number,
        sprites: Sprites,
        goal: Coord2D,
        player: Coord2D,
        facing: Direction,
        obstacles: Obstacle[][] = []
    ): Grid {
        var grid: Obstacle[][] = [];

        // Add ground cover everywhere
        for (var y = 0; y < rows + 2; y++) {
            grid[y] = [];
            for (var x = 0; x < cols + 2; x++) {
                grid[y][x] = new Obstacle(Ground.Clear, [sprites.grass]);
            }
        }

        // Replace the interior with the given level
        for (var y = 0; y < obstacles.length; y++) {
            for (var x = 0; x < obstacles[y].length; x++) {
                grid[y+1][x+1] = obstacles[y][x];
            }
        }

        // Replace the top and bottom, including corners, with walls
        for (var x = 0; x < cols + 2; x++) {
            grid[     0][x] = new Obstacle(Ground.Wall, [sprites.wall.full]);
            grid[rows+1][x] = new Obstacle(Ground.Wall, [sprites.wall.full]);
        }

        // Replace the left and right, excluding corners, with walls
        for (var y = 1; y < rows + 1; y++) {
            grid[y][     0] = new Obstacle(Ground.Wall, [sprites.wall.full]);
            grid[y][cols+1] = new Obstacle(Ground.Wall, [sprites.wall.full]);
        }

        return new Grid(
            rows,
            cols,
            sprites,
            goal,
            player,
            facing,
            grid,
            false
        );
    }

    private constructor(readonly rows: number, readonly cols: number,
        readonly sprites: Sprites, readonly goal: Coord2D,
        readonly playerLocation: Coord2D, readonly facing: Direction,
        private world: Obstacle[][], readonly hasFailed) {}

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
                let tempLoc = this.playerLocation.nextLocation(this.facing);

                switch (this.world[tempLoc.row][tempLoc.col].type) {
                    case (Ground.Clear): {
                        newRow = tempLoc.row;
                        newCol = tempLoc.col;
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

    public inspect(pred: RobotPredicate): boolean {
        switch (pred) {
            case RobotPredicate.ClearInFront: {
                var next = this.playerLocation.nextLocation(this.facing);

                return this.world[next.row][next.col].type == Ground.Clear;
            }
        }
    }

    public render(): string[][][] {
        var grid: string[][][] = [];

        // Fill with ground and obstacle sprites
        for (var y = 0; y < this.rows + 2; y++) {
            grid[y] = [];
            for (var x = 0; x < this.cols + 2; x++) {
                grid[y][x] = [this.sprites.ground, ...this.world[y][x].sprites];
            }
        }

        // Add goal sprite
        grid[this.goal.row]
            [this.goal.col]
            .push(this.sprites.goal);

        // Add player sprite
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
        full: string,
        horizontal: string,
        vertical: string,
        topLeft: string,
        topRight: string,
        bottomLeft: string,
        bottomRight: string
    }
}

}
