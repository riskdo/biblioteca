# Sistema de Gerenciamento de Biblioteca (SGB)

**Aluno:** Ricardo Lopes  
**Disciplina:** Análise e Projeto Orientado a Objetos  
**Data:** 04/09/2025  

---

## 1. Resumo
O sistema implementa cadastro de usuários (**Aluno** e **Professor**), cadastro de livros, empréstimos e devoluções, respeitando os limites:
- Aluno → até **3 livros**
- Professor → até **5 livros**

O sistema também gera relatórios básicos de empréstimos ativos.

---

## 2. Decisões de Modelagem
- **Herança:** `Aluno` e `Professor` herdam de `Usuario`, compartilhando atributos e especializando o método `limite()`.
- **Encapsulamento:** atributos internos foram definidos como privados (`_atributo`), acessados apenas via métodos/propriedades.
- **Polimorfismo:** o método `limite()` foi sobrescrito em `Aluno` e `Professor`, retornando valores diferentes.
- **Associações:** `Emprestimo` associa `Usuario` e `Livro`, contendo datas de retirada e devolução.

---

## 3. Testes Realizados
- **CT01:** Emprestar livro disponível → OK.  
- **CT02:** Emprestar livro já emprestado → Sistema recusou (OK).  
- **CT03:** Aluno tentou pegar mais de 3 livros → Sistema recusou o 4º (OK).  
- **CT05:** Devolver livro → Livro voltou a ficar disponível (OK).  

---

## 4. Conclusão
O projeto seguiu o ciclo **análise → projeto → implementação**.  
Mostrou na prática os conceitos de orientação a objetos: **herança, polimorfismo e encapsulamento**.  

### Possíveis melhorias futuras:
- Controle de **multas por atraso**.  
- Implementação de **reserva de livros**.  
- Criação de uma **interface gráfica ou web**.  
- Integração com banco de dados para persistência.  