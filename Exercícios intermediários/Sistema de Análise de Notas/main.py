import funcoes as f
import dados as d

d.ler_arquivos()
print("Bem-vindo ao cadastro de alunos 2.0")

while True:

    print("1. Cadastrar aluno e notas") 
    print("2. Listar alunos e médias") 
    print("3. Listar aprovados e reprovados") 
    print("4. Listar melhor e pior aluno") 
    print("5. Ordenar alunos por média") 
    print("6. Salvar e sair") 
    f.linha()
    opcao = input("Selecione o número da opção desejada: ")

    if opcao == "1":
        f.cadastro_alunos()

    elif opcao == "2":
        f.listar_alunos()

    elif opcao == "3":
        f.listar_aprovados_reprovados()

    elif opcao == "4":
        f.mostrar_extremos()

    elif opcao == "5":
        f.mostrar_ordem()

    elif opcao == "6":
        d.salvar_arquivos()

    else:
        print("Opção inválida! Escolha um número válido.")