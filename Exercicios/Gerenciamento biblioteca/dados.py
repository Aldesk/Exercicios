import json

emprestimos = []
cadastros = []
caminho = "D:/Andre/workspace/Exercicios/Gerenciamento biblioteca"

def salvar_dados():
    with open(f"{caminho}/livros.json", "w", encoding="utf-8") as arquivo_livros:
        json.dump(cadastros, arquivo_livros, ensure_ascii=False, indent=2)
    with open(f"{caminho}/emprestimos.json", "w", encoding="utf-8") as arquivo_emprestimos:
        json.dump(emprestimos, arquivo_emprestimos, ensure_ascii=False, indent=2)
    print("Dados salvos com sucesso! Encerrando o programa.")

def abre_arquivos():
    try: 
        with open(f"{caminho}/livros.json", "r", encoding="utf-8") as arquivo_livros:
            livros_carregados = json.load(arquivo_livros)
            cadastros.extend(livros_carregados)
        with open(f"{caminho}/emprestimos.json", "r", encoding="utf-8") as arquivo_emprestimos:
            emprestimos_carregados = json.load(arquivo_emprestimos)
            emprestimos.extend(emprestimos_carregados)
    except FileNotFoundError:
        print("Nenhum arquivo de dados anterior encontrado. Iniciando do zero.")