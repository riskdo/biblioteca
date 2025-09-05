class Usuario:
    def __init__(self, nome: str, matricula: str):
        self._nome = nome
        self._matricula = matricula
        self._emprestimos = []

    def limite(self) -> int:
        raise NotImplementedError("Deve ser implementado pelas subclasses")

    def adicionar_emprestimo(self, emprestimo) -> bool:
        if len(self._emprestimos) < self.limite():
            self._emprestimos.append(emprestimo)
            return True
        return False

    def remover_emprestimo(self, emprestimo):
        if emprestimo in self._emprestimos:
            self._emprestimos.remove(emprestimo)

    @property
    def nome(self):
        return self._nome

    @property
    def emprestimos(self):
        return list(self._emprestimos)

    def __str__(self):
        return f"{self._nome} ({self._matricula})"