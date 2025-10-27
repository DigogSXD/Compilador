from parser import NumberNode, BinOpNode

class CodeGenerator:
    def visit(self, node):
        """Método 'visitor' que delega para o método apropriado."""
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def visit_NumberNode(self, node):
        """Gera código para um número."""
        return str(node.value)

    def visit_BinOpNode(self, node):
        """Gera código para uma operação binária."""
        left_code = self.visit(node.left_node)
        right_code = self.visit(node.right_node)
        op = node.op_token.value
        # Adicionar parênteses garante a precedência correta no código gerado
        return f"({left_code} {op} {right_code})"

    def generic_visit(self, node):
        raise RuntimeError(f'Nenhum método visit_{type(node).__name__} definido')