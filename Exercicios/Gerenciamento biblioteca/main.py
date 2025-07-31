import dados as d
import funcoes as f

d.abre_arquivos()
print("----Bem-vindo(a) ao programa de gerenciamento de livros!----")
while True:

    print("-----------------------------------")
    print("[1] Adicionar novo livro")
    print("[2] Adicionar livro já existente")
    print("[3] Listar livros")
    print("[4] Registrar empréstimo")
    print("[5] Listar empréstimos")
    print("[6] Registrar devolução")
    print("[7] Salvar e sair")
    print("-----------------------------------")
    opcao = input("Selecione a opção desejada: ")

    if opcao == "1":
        print("-----------------------------------")
        f.adicionar_livro()

    elif opcao == "2":
        print("-----------------------------------")
        f.adicionar_repetido()
        print("-----------------------------------")

    elif opcao == "3":
        print("-----------------------------------")
        f.listar_livros()
    
    elif opcao == "4":
        print("-----------------------------------")
        f.emprestar_livros()

    elif opcao == "5":
        print("-----------------------------------")
        f.listar_emprestimos()
    
    elif opcao == "6":
        print("-----------------------------------")
        f.devolver_livros()
    
    elif opcao == "7":
        d.salvar_dados()
        break
    else:
        print("opção inválida")
        print("-----------------------------------")