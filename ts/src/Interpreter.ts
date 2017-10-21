namespace Interpreter {
    export function* runInterpreter
      ( world: World.Grid
      , ast: PS.Types.AST
      , env: Array<PS.Types.Environment>
      ): IterableIterator<World.Grid>
    {
        var res = PS.Interpreter.runInterpreter(world)(ast)(env);
        var curr;

        while(curr = PS.Interpreter.nextResume(res)) {
          yield curr.value;
          res = curr.resume;
        }
    }
    export function astCost(ast: PS.Types.AST): number {
        return PS.Interpreter.astCost(ast);
    }
}
