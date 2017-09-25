namespace Main {

export function runGame(grid: World.Grid, code: String) {
    return Parser.parseAST([], null as Purescript.Types.Environment, code);
    // TODO: return the game with the returned AST, passing it to the
    // interpreter.
}

}
