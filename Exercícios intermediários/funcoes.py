import dados as d
from functools import reduce

def alunos_false():
    if not d.alunos:
        linha()
        print("Sem alunos cadastrados, tente cadastrar um alunos primeiro")
        linha()

def calcular_media(notas):
    return sum(notas)/len(notas)

def linha():
    print("-" * 40)

def cadastro_alunos():
    linha()
    print("Você acessou o cadastro de alunos")
    notas = []
    nome = input("Digite o nome do aluno que deseja cadastrar: ")
    while True:
        try:
            linha()
            nota = float(input("Digite a nota do estudante: "))
            if not 0 <= nota <= 10:
                continue
            notas.append(nota)
            novanota = True
        except ValueError:
            linha()
            print("Valor inválido para notas")
            continue
        while True:
            linha()
            print("Nota adicionada com sucesso!")
            confirma = input("Adicionar nova nota? (S/N): ").lower()
            if confirma == "n":
                novanota = False
                break
            elif confirma == "s":
                break
            else:
                print("Opção inválida, tente usar 'S' para sim ou 'N' para não")
        if not novanota:
            break
    media = calcular_media(notas)
    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media
        }
    d.alunos.append(aluno)

def listar_alunos():
    alunos_false()
    if d.alunos:
        linha()
        print("Esta é a lista dos alunos cadastrados e suas médias: ")
        linha()
        for i, aluno in enumerate(d.alunos, start=1):
            print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")
        linha()

def listar_aprovados_reprovados():
    alunos_false()
    if d.alunos:
        total = reduce(lambda a, aluno: a + aluno["media"], d.alunos, 0) #primeiro termo do lambda é o acúmulo, no caso "a", segundo termo é o iterado
        media_geral = total/len(d.alunos)
        aprovados = filter(lambda aluno: aluno["media"] >= media_geral, d.alunos)
        reprovados = filter(lambda aluno: aluno["media"] < media_geral, d.alunos)
        linha()
        print("Lista de alunos aprovados:")
        for i, aluno in enumerate(aprovados, start=1):
            print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")
        linha()
        print("Lista de alunos reprovados:")
        for i, aluno in enumerate(reprovados, start=1):
            print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")
        linha()

def ordenar_lista(lista):
    return sorted(lista, key=lambda aluno: aluno["media"])

def mostrar_ordem():
    ordem = ordenar_lista(d.alunos)
    for i, aluno in enumerate(ordem, start=1):
        print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")

def mostrar_extremos():
    alunos_false()
    if d.alunos:
        linha()
        ordenada = ordenar_lista(d.alunos)
        print(f"Melhor média: {ordenada[-1]['nome']} - {ordenada[-1]['media']:.2f}")
        print(f"Pior média: {ordenada[0]['nome']} - {ordenada[0]['media']:.2f}")