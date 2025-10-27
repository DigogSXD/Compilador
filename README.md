# Mini Compilador de Expressões Aritméticas

Este é um projeto simples em Python que demonstra as fases fundamentais de um compilador para avaliar expressões aritméticas. Ele pega uma string contendo uma expressão matemática, a processa através de um analisador léxico (lexer), um analisador sintático (parser) que constrói uma Árvore Sintática Abstrata (AST), e finalmente um gerador de código que produz uma string executável.

## Funcionalidades

-   Suporte para as quatro operações básicas: adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`).
-   Respeito pela precedência de operadores (multiplicação e divisão são executadas antes de adição e subtração).
-   Suporte para o uso de parênteses (`()`) para agrupar expressões e alterar a ordem de prioridade.
-   Implementação clara e separada das três fases principais de um compilador.

## Como Funciona

O processo de compilação é dividido em três etapas principais, orquestradas pelo `main.py`:

### 1. Análise Léxica (`lexer.py`)

A primeira fase, conhecida como *lexing* ou *tokenization*. O código fonte (a string da expressão) é lido e quebrado em uma sequência de "tokens". Cada token representa uma unidade fundamental da linguagem, como um número, um operador ou um parêntese.

Por exemplo, a expressão `15 + 20` é transformada em:
`[Token(NUMERO, '15'), Token(MAIS, '+'), Token(NUMERO, '20')]`

### 2. Análise Sintática (`parser.py`)

O parser recebe a lista de tokens e verifica se eles seguem as regras gramaticais da linguagem. Ele organiza os tokens em uma estrutura de árvore chamada **Árvore Sintática Abstrata (AST)**. A AST representa a estrutura hierárquica da expressão, respeitando a precedência dos operadores.

Por exemplo, a expressão `20 * 2` se tornaria um nó de operação binária com `*` como operador e `20` e `2` como filhos.

### 3. Geração de Código (`codegen.py`)

A fase final percorre a AST (usando o padrão de projeto *Visitor*) e traduz cada nó em uma string de código equivalente. O resultado é uma nova string que representa a expressão original, mas com a estrutura e a precedência de operações tornadas explícitas através de parênteses. Esta string final pode ser facilmente avaliada por um interpretador (neste caso, a função `eval()` do Python).

## Estrutura dos Arquivos

-   `main.py`: O ponto de entrada do programa. Orquestra a execução das três fases e exibe o resultado.
-   `lexer.py`: Contém a lógica para a análise léxica (tokenização) usando expressões regulares.
-   `parser.py`: Define as classes para os nós da AST e a lógica do parser que constrói a árvore a partir dos tokens.
-   `codegen.py`: Implementa o gerador de código que converte a AST em uma string de código final.

## Como Executar

1.  Certifique-se de ter o **Python 3** instalado.
2.  Salve os quatro arquivos (`main.py`, `lexer.py`, `parser.py`, `codegen.py`) no mesmo diretório.
3.  Execute o arquivo principal através do terminal:

```bash
python main.py
