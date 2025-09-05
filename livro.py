class Livro:
    def __init__(self, titulo: str, autor: str):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = True

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    def emprestar(self) -> bool:
        if self._disponivel:
            self._disponivel = False
            return True
        return False

    def devolver(self):
        self._disponivel = True

    def __str__(self):
        return f"'{self._titulo}' de {self._autor}"