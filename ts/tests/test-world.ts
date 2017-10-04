import { expect } from 'chai';
import 'mocha';

describe('Testing movement', () => {
    it('TurnLeft maintains position and changes facing', () => {
        let w = new World.Grid(8, 8, new World.Coord2D(2, 3),
            new World.Coord2D(3, 4), World.Direction.Up);
        let directions = [World.Direction.Up,
            World.Direction.Left,
            World.Direction.Down,
            World.Direction.Right,
            World.Direction.Up];
        for (let dir of directions) {
            expect(w.playerLocation).to.eql(new World.Coord2D(3, 4));
            expect(w.facing).to.equal(dir);
            w = w.step(World.PlayerAction.TurnLeft);
        }
    });

    it('TurnRight maintains position and changes facing', () => {
        let w = new World.Grid(8, 8, new World.Coord2D(2, 3),
            new World.Coord2D(5, 6), World.Direction.Up);
        let directions = [World.Direction.Up,
            World.Direction.Right,
            World.Direction.Down,
            World.Direction.Left,
            World.Direction.Up];
        for (let dir of directions) {
            expect(w.playerLocation).to.eql(new World.Coord2D(5, 6));
            expect(w.facing).to.equal(dir);
            w = w.step(World.PlayerAction.TurnRight);
        }
    });

    it('WalkForward moves in correct direction', () => {
        let facingDir = [World.Direction.Up,
            World.Direction.Right,
            World.Direction.Left,
            World.Direction.Down];
        // Always start at (2, 6).
        let finalPos = [new World.Coord2D(1, 6),
            new World.Coord2D(2, 7),
            new World.Coord2D(2, 5),
            new World.Coord2D(3, 6)];
        for (let i in facingDir) {
            let w = new World.Grid(8, 8, new World.Coord2D(2, 3),
                new World.Coord2D(2, 6), facingDir[i]);
            let newGrid = w.step(World.PlayerAction.WalkForward);
            expect(newGrid.facing).to.equal(facingDir[i]);
            expect(newGrid.playerLocation).to.eql(finalPos[i]);
        }
    });
});

describe('Victory and failure conditions', () => {
    it("Haven't won or lost at start (in general)", () => {
        let w = new World.Grid(8, 8, new World.Coord2D(2, 3),
            new World.Coord2D(5, 6), World.Direction.Up);
        expect(w.victory()).to.be.false;
        expect(w.failed()).to.be.false;
    });

    it("Win when moving onto goal square", () => {
        let w = new World.Grid(8, 8, new World.Coord2D(4, 6),
            new World.Coord2D(5, 6), World.Direction.Up);
        expect(w.victory()).to.be.false;
        let newGrid = w.step(World.PlayerAction.WalkForward);
        expect(newGrid.victory()).to.be.true;
    });

    it('Lose when walk off the grid', () => {
        let facingDir = [World.Direction.Up,
            World.Direction.Right,
            World.Direction.Left,
            World.Direction.Down];
        let initialPos = [new World.Coord2D(0, 6),
            new World.Coord2D(2, 7),
            new World.Coord2D(2, 0),
            new World.Coord2D(7, 6)];
        for (let i in facingDir) {
            let w = new World.Grid(8, 8, new World.Coord2D(2, 3),
                initialPos[i], facingDir[i]);
            expect(w.failed()).to.be.false;
            let newGrid = w.step(World.PlayerAction.WalkForward);
            expect(newGrid.failed()).to.be.true;
        }
    });
});

describe('Grid rendering', () => {
    const sprites = {
        grass: function(): string {
            return 'grass';
        },
        player: {
            Up: 'Up',
            Down: 'Down',
            Left: 'Left',
            Right: 'Right'
        },
        goal: 'GOAL'
    };

    it('Grass everywhere', () => {
        let numRows = 8;
        let numCols = 9;
        let w = new World.Grid(numRows, numCols, new World.Coord2D(2, 3),
            new World.Coord2D(3, 4), World.Direction.Up);
        let render = w.render(sprites);
        for (let row of render) {
            for (let cell of row) {
                expect(cell).to.contain('grass');
            }
        }
    });

    it('Goal only at corresponding location', () => {
        let w = new World.Grid(8, 9, new World.Coord2D(2, 3),
            new World.Coord2D(3, 4), World.Direction.Up);
        let render = w.render(sprites);
        expect(render[2][3]).to.contain('GOAL');
        expect(render[0][0]).not.to.contain('GOAL');
        expect(render[3][4]).not.to.contain('GOAL');
    });

    it('Robot at correct location with correct orientation', () => {
        let directions = [World.Direction.Up,
            World.Direction.Left,
            World.Direction.Down,
            World.Direction.Right];
        let dirSprites = ['Up', 'Left', 'Down', 'Right'];

        for (let i in directions) {
            let w = new World.Grid(8, 9, new World.Coord2D(2, 3),
                new World.Coord2D(3, 4), directions[i]);
            let render = w.render(sprites);
            expect(render[3][4]).to.contain(dirSprites[i]);
        }
    });
});