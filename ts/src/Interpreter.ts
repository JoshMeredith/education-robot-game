namespace Interpreter {
    export function* runInterpreter
      ( world: World.Grid
      , ast: Purescript.Types.AST
      , env: Array<Purescript.Types.Environment>
      ): IterableIterator<World.Grid>
    {
        var res = Purescript.Interpreter.runInterpreter(world)(ast)(env);
        var curr;

        while(curr = Purescript.Interpreter.nextResume(res)) {
          yield curr.value;
          res = curr.resume;
        }
    }
}
