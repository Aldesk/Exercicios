import json
import funcoes as f

alunos = []
caminho = "D:/Andre/workspace/Exercícios intermediários/Sistema de Análise de Notas"

def salvar_arquivos():
    with open(f"{caminho}/alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=2)
    print("Dados salvos com sucesso! Encerrando programa.")

def ler_arquivos():
    try:    
        with open(f"{caminho}/alunos.json", "r", encoding="utf-8") as arquivo:
            alunos_carregados = json.load(arquivo)
            alunos.extend(alunos_carregados)
    except FileNotFoundError:
        print("Nenhum arquivo de dados encontrado! Iniciando novo registro...")
        f.linha()