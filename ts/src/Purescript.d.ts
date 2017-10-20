export as namespace PS;

export namespace Interpreter {
    export var testNum: number;
    export function runInterpreter
      (world: World.Grid):
      (ast: Types.AST) =>
      (environment: Array<Types.Environment>) =>
      Types.Resume
    export function nextResume(resume: Types.Resume):
      {value: World.Grid, resume: Types.Resume} | null;
    export var environment:
      { turnLeft    : Types.Environment
      , turnRight   : Types.Environment
      , walkForward : Types.Environment
      , moveLeft    : Types.Environment
      , moveRight   : Types.Environment
      , moveUp      : Types.Environment
      , moveDown    : Types.Environment
      }
    export function astCost(ast: Types.AST): number;
}

export namespace Parser {
    export function parseAST
      (features: Array<Types.LanguageExtras>):
      (environment: Array<Types.Environment>) =>
      (code: String) =>
      { ast: Types.AST | null
      , messages: Array<String>
      , names: Array<String>
      };

    export function prettyPrint(a: Types.AST): string;
}

export namespace Types {
    export class AST {}
    export class LanguageExtras {}
    export class Environment {}
    export class Resume {}
}
