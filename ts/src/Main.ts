namespace Main {

export function runGame(grid: World.Grid, code: String) {
    return Parser.parseAST([], [], code);
    // TODO: return the game with the returned AST, passing it to the
    // interpreter.
}

}
