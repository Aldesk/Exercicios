import dados as d
import funcoes as f
d.abre_arquivos()
print("------------Bem-vindo ao cadastro de estudantes------------")

while True:

    print("///////////////////////////////////////////////////////////")
    print("[1] ➡ Adicionar aluno e notas")
    print("[2] ➡ Listar todos os alunos e médias")
    print("[3] ➡ Buscar aluno pelo nome")
    print("[4] ➡ Apagar estudante da lista")
    print("[5] ➡ Salvar e sair")
    print("///////////////////////////////////////////////////////////")
    opcao = input("Selecione uma opção: ")

    if opcao == "1": 
        cadastro = f.adicionar_aluno()
        d.cadastros.append(cadastro)

    elif opcao == "2": 
        f.mostrar_cadastros()

    elif opcao == "3": 
        f.buscar_alunos()

    elif opcao == "4":
        f.apaga_aluno()

    elif opcao == "5": 
        d.salva_arquivo()
        break

    else:
        print("Opção inválida, tente um dos números das opções disponíveis")            