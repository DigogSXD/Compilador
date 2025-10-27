import re
from collections import namedtuple

# Define a estrutura de um Token
Token = namedtuple('Token', ['type', 'value'])

# Define os padrões (regex) para cada tipo de token
TOKEN_PATTERNS = [
    ('NUMERO',  r'\d+'),           # Números inteiros
    ('MAIS',    r'\+'),            # Operador de soma
    ('MENOS',   r'-'),             # Operador de subtração
    ('MULT',    r'\*'),            # Operador de multiplicação
    ('DIV',     r'/'),             # Operador de divisão
    ('LPAREN',  r'\('),            # Parêntese esquerdo (CORRIGIDO)
    ('RPAREN',  r'\)'),            # Parêntese direito (CORRIGIDO)
    ('ESPACO',  r'\s+'),           # Espaços em branco (para ignorar)
    ('ERRO',    r'.'),             # Qualquer outro caractere é um erro
]

# Compila a expressão regular completa
TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_PATTERNS)

def lexer(code):
    """
    Recebe uma string de código e retorna uma lista de Tokens.
    """
    tokens = []
    for mo in re.finditer(TOKEN_REGEX, code):
        kind = mo.lastgroup
        value = mo.group()
        
        if kind == 'ESPACO':
            # Ignora espaços em branco
            continue
        elif kind == 'ERRO':
            raise RuntimeError(f'Caractere inesperado: {value}')
        
        tokens.append(Token(kind, value))
        
    return tokens