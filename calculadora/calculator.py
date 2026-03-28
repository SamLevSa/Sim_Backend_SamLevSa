class Calculator:
    def add(self, a: float, b: float) -> float:
        """Metodo ja implementado para servir de exemplo."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Método implementado pelo aluno."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Método implementado pelo aluno."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Método implementado pelo aluno."""
        if b == 0:
            raise ValueError("Impossível dividir por 0")
        return a / b