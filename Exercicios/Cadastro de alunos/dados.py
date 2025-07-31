import json
cadastros = []
nao = ["nao", "não", "no", "n", "nã", "ão"]

def salva_arquivo(): #Salva o arquivo e sai do programa
    with open("D:/Andre/workspace/Exercicios/Cadastro de alunos/alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso! Encerrando o programa.")

def abre_arquivos(): #Tenta abrir arquivo salvo
    try: 
        with open("D:/Andre/workspace/Exercicios/Cadastro de alunos/alunos.json", "r", encoding="utf-8") as arquivo:
            dados_carregados = json.load(arquivo)
            cadastros.extend(dados_carregados)
    except FileNotFoundError:
        print("Nenhum arquivo de dados anterior encontrado. Iniciando do zero.")