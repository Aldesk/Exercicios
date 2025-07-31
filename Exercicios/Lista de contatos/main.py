contatos = []

print("-------Bem-vindo à sua lista de contatos!!-------")

while True:

    print("---------------selecione uma opção---------------")
    print("[1] Adicionar contato")
    print("[2] Listar contatos")
    print("[3] Buscar contato pelo nome")
    print("[4] Remover contato")
    print("[5] Sair do programa")  
    print("-------------------------------------------------")
    print("-------------------------------------------------")

    opcao = input("Selecione a opção desejada: ")
    
    if opcao == "1": #Adicionar contato
        nome = input("Adicione o nome do novo contato: ")
        tel = input("Adicione o número do novo contato: ")
        email = input("Adicione o e-mail do novo contato: ")
        contatos.append({
            "nome": nome,
            "tel": tel,
            "email": email
        })
        print("Contato salvo com sucesso")

    elif opcao == "2": #Listar contatos
        if len(contatos) == 0:
            print("Sem contatos salvos")
        else:
            for i, contato in enumerate(contatos, start=1):
                print(f"{i}. {contato["nome"]} - {contato["tel"]} - {contato["email"]}")
                        
    elif opcao == "3": #Buscar contato pelo nome
        if len(contatos) == 0:
            print("Sem contatos salvos")
        else:
            busca = input("Digite o nome do contato que deseja buscar: ").strip()
            encontrado = False
            for i, contato in enumerate(contatos, start=1):
                if busca.lower() in contato["nome"].lower():
                    print(f"{i}. {contato["nome"]} - {contato["tel"]} - {contato["email"]}")
                    if i == len(contatos):
                        for contato in contatos:
                            encontrado = True
                        if not encontrado:
                            print("Contato não encontrado!")

    elif opcao == "4": #Remover contato
        if len(contatos) == 0:
            print("Sem contatos salvos")
        else:
            for i, contato in enumerate(contatos, start=1):
                print(f"{i}. {contato["nome"]} - {contato["tel"]} - {contato["email"]}")
            rem = input("Selecione o contato a ser excluído: ")
            remove = rem.isdigit()
            if remove:
                print(f"O contato {contatos[int(rem)-1]["nome"]} foi excluído!")
                contatos(int(rem)-1).pop
            else:
                print("Número de contato inválido")

    elif opcao == "5": #Sair do programa
        print("Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida")