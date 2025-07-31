import dados as d

def calcular_media(lista_de_notas):
    if not lista_de_notas:
        return 0
    return sum(lista_de_notas)/len(lista_de_notas)

def adicionar_aluno(): #Cadastra alunos e notas
    nome = input("Digite o nome do estudante: ")
    notas = []
    while True:
        try:
            novanota = float(input("Adicione a nota do estudante: "))
            notas.append(novanota)
        except ValueError:
            print("Nota inválida, digite um número!")
            continue
        continua = input("Deseja adicionar uma nova nota? ").lower().strip()
        if continua in d.nao:
            break

    media = calcular_media(notas)
    return {
        "nome": nome,
        "notas": notas,
        "media": media
    }

def mostrar_cadastros(): #Mostra alunos e suas médias
    alunos_vazios()
    if d.cadastros:
        for i, cadastro in enumerate(d.cadastros, start=1):
            print(f"{i}. {cadastro["nome"]} - média: {cadastro["media"]}")

def alunos_vazios():
    if not d.cadastros:
        print("A lista de estudantes está vazia, tente adicionar um cadastro")

def buscar_alunos(): #Busca de alunos cadastrados pelo nome
    alunos_vazios()
    if d.cadastros:
        busca = input("Digite o nome do estudante: ").lower().strip()
        encontrado = False
        for i, cadastro in enumerate(d.cadastros, start=1):
            if busca in cadastro["nome"].lower():
                print(f"{i}. {cadastro["nome"]} - Média: {cadastro["media"]}")
                encontrado = True
        if not encontrado:
            print("Contato não encontrado")

def apaga_aluno():
    alunos_vazios()
    if d.cadastros:
        for i, cadastro in enumerate(d.cadastros, start=1):
            print(f"{i}. {cadastro["nome"]} - média: {cadastro["media"]}")
        while True:
            try:
                rem = int(input("escolha o aluno que quer remover da lista: "))
                d.cadastros.pop(rem-1)
                print("Aluno removido com sucesso!")
                break
            except IndexError:
                print("Valor inválido, tente novamente!")