from datetime import date, timedelta

class Emprestimo:
    def __init__(self, usuario, livro, prazo_dias: int = 7):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = date.today()
        self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=prazo_dias)
        self.data_devolvido = None

    def __str__(self):
        devolvido = self.data_devolvido if self.data_devolvido else "—"
        return (f"{self.usuario} -> {self.livro} | "
                f"emprestado: {self.data_emprestimo} | prazo: {self.data_devolucao_prevista} | devolvido: {devolvido}")