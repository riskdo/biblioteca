from emprestimo import Emprestimo

def emprestar_livro(usuario, livro):
    if not livro.disponivel:
        print("Falha: livro já emprestado.")
        return None
    if len(usuario.emprestimos) >= usuario.limite():
        print(f"Falha: {usuario.nome} atingiu o limite de empréstimos ({usuario.limite()}).")
        return None

    if livro.emprestar():
        e = Emprestimo(usuario, livro)
        if usuario.adicionar_emprestimo(e):
            print("Empréstimo realizado:", e)
            return e
        else:
            livro.devolver()
            print("Falha ao registrar empréstimo no usuário.")
            return None
    print("Falha ao alterar disponibilidade do livro.")
    return None


def devolver_livro(usuario, livro):
    alvo = None
    for e in usuario.emprestimos:
        if e.livro is livro and e.data_devolvido is None:
            alvo = e
            break

    if not alvo:
        print("Falha: empréstimo não encontrado para este usuário/livro.")
        return False

    alvo.data_devolvido = True
    usuario.remover_emprestimo(alvo)
    livro.devolver()
    print("Devolução realizada:", alvo)
    return True
