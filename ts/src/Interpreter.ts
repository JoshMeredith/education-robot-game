namespace Interpreter {
    class Gen {
        public value: World.Grid;
        constructor(private resume: Purescript.Types.Resume) {}
        public next() {
            var g = Purescript.Interpreter.nextResume(this.resume);
            this.value = g.value;
            this.resume = g.resume;
        }
    }

    export function runInterpreter
      ( world: World.Grid
      , ast: Purescript.Types.AST
      , env: Array<Purescript.Types.Environment>
      ): Gen
    {
        var res = Purescript.Interpreter.runInterpreter(world)(ast)(env);
        return new Gen(res);
    }
}
