namespace Main {

export function runGame(grid: World.Grid, code: String) {
    let ast = Parser.parseAST([], [], code).ast;
    console.log(ast);
    console.log(grid);
    let interpreterGen = Interpreter.runInterpreter(grid, ast, [
        PS.Interpreter.environment.moveLeft]);
    for (let curGrid of interpreterGen) {
        console.log(curGrid.playerFacing());
        console.log(curGrid.playerLocation);
        console.log(curGrid.victory());
    }
}

}
