namespace Parser {
    export function parseAST
      ( features: Array<PS.Types.LanguageExtras>
      , environment: Array<PS.Types.Environment>
      , code: String
      ):
      { ast: PS.Types.AST | null
      , messages: Array<String>
      , names: Array<String>
      }
    {
        return PS.Parser.parseAST(features)(environment)(code);
    }

    export function prettyPrint(a: PS.Types.AST): string {
        return PS.Parser.prettyPrint(a);
    }
}
