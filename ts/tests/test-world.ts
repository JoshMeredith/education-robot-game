import { expect } from 'chai';
import 'mocha';

let x = new World.Coord2D(2, 4);

describe('Ensure coordinates work', () => {
    it('check comp', () => {
        expect(x.row).to.equal(2);
        expect(x.col).to.equal(4);
    });
});
