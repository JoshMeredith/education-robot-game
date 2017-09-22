export as namespace Purescript;

export namespace Interpreter {
    export var testNum: number;
}

export namespace Parser {
    export function parseAST
      (features: Array<Types.LanguageExtras>):
      (environment: Types.Environment) =>
      (code: String) =>
      { ast: Types.AST | null
      , messages: Array<String>
      , names: Array<String>
      };

}

export namespace Types {
    export class AST {}
    export class LanguageExtras {}
    export class Environment {}
}
