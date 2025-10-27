from lexer import lexer
from parser import Parser
from codegen import CodeGenerator

if __name__ == "__main__":
    # Código que será compilado
    codigo_fonte = "15 + (20 * 2) - 10 / 5"
    
    try:
        print(f"Código Fonte: '{codigo_fonte}'\n")
        
        # 1. Fase de Análise Léxica (Lexer)
        tokens = lexer(codigo_fonte)
        print(f"Tokens: {tokens}\n")
        
        # 2. Fase de Análise Sintática (Parser)
        parser = Parser(tokens)
        ast = parser.parse()
        print(f"AST: {ast}\n")
        
        # 3. Fase de Geração de Código (Code Generator)
        generator = CodeGenerator()
        codigo_compilado = generator.visit(ast)
        print(f"Código Compilado: '{codigo_compilado}'\n")
        
        # 4. Execução do código gerado para verificar o resultado
        resultado = eval(codigo_compilado)
        print(f"Resultado da Execução: {resultado}")

    except RuntimeError as e:
        print(f"Erro durante a compilação: {e}")