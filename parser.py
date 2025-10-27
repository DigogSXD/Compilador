from lexer import Token

# --- Classes que representam os nós da Árvore Sintática Abstrata (AST) ---
class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = int(token.value)

    def __repr__(self):
        return f"Number({self.value})"

class BinOpNode:
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node

    def __repr__(self):
        return f"({self.left_node} {self.op_token.type} {self.right_node})"

# --- O Parser ---
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.current_token = None
        self.advance()

    def advance(self):
        """Avança para o próximo token na lista."""
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
        else:
            self.current_token = None # Fim dos tokens

    def parse(self):
        """Inicia o processo de parsing."""
        if not self.current_token:
            return None
        ast = self.expression()
        if self.current_token is not None:
            raise RuntimeError(f"Erro de sintaxe: Token inesperado no final: {self.current_token}")
        return ast

    def factor(self):
        """Regra: fator -> NUMERO | LPAREN expressao RPAREN"""
        token = self.current_token
        if token.type == 'NUMERO':
            self.advance()
            return NumberNode(token)
        elif token.type == 'LPAREN':
            self.advance()
            node = self.expression()
            if not self.current_token or self.current_token.type != 'RPAREN':
                raise RuntimeError("Erro de sintaxe: Esperava um ')'")
            self.advance() # Consome o ')'
            return node
        
        raise RuntimeError(f"Erro de sintaxe: Token inesperado: {token}")

    def term(self):
        """Regra: termo -> fator ((MULT | DIV) fator)*"""
        node = self.factor()
        while self.current_token and self.current_token.type in ('MULT', 'DIV'):
            op_token = self.current_token
            self.advance()
            right = self.factor()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=right)
        return node

    def expression(self):
        """Regra: expressao -> termo ((MAIS | MENOS) termo)*"""
        node = self.term()
        while self.current_token and self.current_token.type in ('MAIS', 'MENOS'):
            op_token = self.current_token
            self.advance()
            right = self.term()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=right)
        return node