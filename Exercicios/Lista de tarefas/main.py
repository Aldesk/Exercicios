listaTarefas = []

print("-------Bem-vindo à sua lista de afazeres-------")
print("-------Por favor, selecione uma opção:---------")
while True:    
    print("///////////////////////////////////////////////")
    print("///////////////////////////////////////////////")
    print("[1] Adicionar nova tarefa")
    print("[2] Listar todas as tarefas")
    print("[3] Marcar tarefa como concluída")
    print("[4] Remover tarefa")
    print("[5] Sair do programa")

    opcao = (input("Digite a opção: "))

    if opcao == "1":
        titulo = input("Anote sua tarefa: ")
        listaTarefas.append({
        "titulo": titulo,
        "estado": True
        })

    elif opcao == "2":
        if len(listaTarefas) == 0:
            print("Sem tarefas cadastradas")
        else:
            for i, n in enumerate(listaTarefas, start=1):
                status = "[ ]" if n["estado"] else "[x]"
                print(f"{i}. {status} {n['titulo']}")

    elif opcao == "3":
        if len(listaTarefas) == 0:
            print("Sem tarefas cadastradas")
        else:
            for i, n in enumerate(listaTarefas, start=1):
                status = "[ ]" if n["estado"] else "[x]"
                print(f"{i}. {status} {n['titulo']}")

            num = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            if 1 <= num <= len(listaTarefas):
                 listaTarefas[num-1]["estado"] = False
                 print(f"Tarefa '{listaTarefas[num-1]["titulo"]}' marcada como concluída")
            else:
                 print("Tarefa inválida")

    elif opcao == "4":
        if len(listaTarefas) == 0:
            print("Sem tarefas cadastradas")
        else:
            for i, n in enumerate(listaTarefas, start=1):
                status = "[ ]" if n["estado"] else "[x]"
                print(f"{i}. {status} {n['titulo']}")

        num = int(input("Digite o número da tarefa que deseja excluir: "))
        if 1 <= num <= len(listaTarefas):
            print(f"Tarefa {listaTarefas[num-1]["titulo"]} removida.")                  
            listaTarefas.pop(num-1)
        else:
            print("Tarefa inválida")

    elif opcao == "5":
        print("Obrigado por usar o programa!")
        break
    else:
         print("opção inválida")