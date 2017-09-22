namespace Parser {
    export function parseAST
      ( features: Array<Purescript.Types.LanguageExtras>
      , environment: Purescript.Types.Environment
      , code: String
      ):
      { ast: Purescript.Types.AST | null
      , messages: Array<String>
      , names: Array<String>
      }
    {
        return Purescript.Parser.parseAST(null)(null)(code);
    }
}
