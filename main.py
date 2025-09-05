from aluno import Aluno
from professor import Professor
from livro import Livro
from servicos import emprestar_livro, devolver_livro

if __name__ == "__main__":
    aluno = Aluno("Ricardo", "A001")
    prof = Professor("Carla", "P001")

    l1 = Livro("Python para Iniciantes", "Fulano")
    l2 = Livro("POO em Python", "Beltrano")
    l3 = Livro("Algoritmos", "Ciclano")
    l4 = Livro("Estruturas de Dados", "Fulana")

    print("\nCT01: Emprestar livro disponível")
    e1 = emprestar_livro(aluno, l1)

    print("\nCT02: Emprestar mesmo livro")
    e2 = emprestar_livro(prof, l1)

    print("\nCT03: Aluno tentar pegar mais de 3 livros")
    emprestar_livro(aluno, l2)
    emprestar_livro(aluno, l3)
    emprestar_livro(aluno, l4)  # deve falhar

    print("\nCT05: Devolver livro")
    devolver_livro(aluno, l1)
