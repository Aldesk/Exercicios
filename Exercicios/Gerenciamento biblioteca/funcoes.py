import dados as d

def not_cadastros():
    if not d.cadastros:
        print("Sem livros cadastrados!")

def not_emprestimos():
    if not d.emprestimos:
        print("Sem livros emprestados!")

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    while True:
        try:    
            ano = int(input("Digite o ano de publicaçao: "))
            break
        except ValueError:
            print("Digite um ano válido!")
    while True:
        try:    
            qtd = int(input("Digite a quantidade de exemplares: "))
            break
        except ValueError:
            print("Digite um valor válido!")
    cadastro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "qtd": qtd
        }
    d.cadastros.append(cadastro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    not_cadastros()
    if d.cadastros:
        for i, cadastro in enumerate(d.cadastros, start=1):
            print(f"{i}. {cadastro['titulo']} - {cadastro['autor']}\nano: {cadastro['ano']}\nexemplares: {cadastro['qtd']}")

def emprestar_livros():
    not_cadastros()
    if d.cadastros:
        print("Você acessou o gerenciamento de empréstimos de livro!")
        print("-----------------------------------")
        nome = input("Digite o seu nome: ")
        print("-----------------------------------")
        print("Selecione o livro que deseja pegar emprestado: ")
        print("-----------------------------------")
        for i, cadastro in enumerate(d.cadastros, start=1):
            print(f"{i}. {cadastro['titulo']} - {cadastro['autor']}\nano: {cadastro['ano']}\nexemplares: {cadastro['qtd']}")
        while True:    
            try:
                num = int(input("Número do livro: "))
            except ValueError:
                print("-----------------------------------")
                print("Número inválido! Tente novamente")
                print("-----------------------------------")
            if 1 <= num <= len(d.cadastros):
                break
            else:
                print("-----------------------------------")
                print("Número inválido! Tente novamente")
                print("-----------------------------------")    
        d.cadastros[num-1]["qtd"] = d.cadastros[num-1]["qtd"]-1
        e_titulo = d.cadastros[num-1]["titulo"]
        e_autor = d.cadastros[num-1]["autor"]
        e_ano = d.cadastros[num-1]["ano"]
        emprestimo = {
            "nome": nome,
            "titulo": e_titulo,
            "autor": e_autor,
            "ano": e_ano
        }
        d.emprestimos.append(emprestimo)
        print("Empréstimo cadastrado com sucesso!")

def listar_emprestimos():
    not_emprestimos()
    if d.emprestimos:
        for i, emprestimo in enumerate(d.emprestimos, start=1):
            print(f"{i}. {emprestimo['nome']}\n{emprestimo['titulo']} - {emprestimo['autor']}\nano: {emprestimo['ano']}")

def devolver_livros():
    not_emprestimos()
    if d.emprestimos:
        print("Selecione o empréstimo que deseja encerrar:")
        print("Você acessou o gerenciamento de devoluções de livros!")
        for i, emprestimo in enumerate(d.emprestimos, start=1):
            print(f"{i}. {emprestimo['nome']}\n{emprestimo['titulo']} - {emprestimo['autor']}\nano: {emprestimo['ano']}")
        while True:
            try:
                num = int(input("Número do livro: "))
            except ValueError:
                print("-----------------------------------")
                print("Número inválido! Tente novamente")
                print("-----------------------------------")
            if 1 <= num <= len(d.emprestimos):
                break
            else:
                print("-----------------------------------")
                print("Número inválido! Tente novamente")
                print("-----------------------------------")
        busca = d.emprestimos[num-1]["titulo"]
        for cadastro in d.cadastros:
            if busca.strip().lower() in cadastro["titulo"].lower():
                cadastro["qtd"] = cadastro["qtd"] + 1    
        d.emprestimos.pop(num-1)
        print("Devolução registrada com sucesso!")

def adicionar_repetido():
    listar_livros()
    while True:
        try:
            ind = int(input("Digite o número do livro que deseja adicionar: "))
        except ValueError:
            print("-----------------------------------")
            print("Número inválido! Tente novamente")
            print("-----------------------------------")
        if 1 <= ind <= len(d.cadastros):
            break
        else:
            print("-----------------------------------")
            print("Número inválido! Tente novamente")
            print("-----------------------------------")
    while True:
        try:
            n = int(input("Digite a quantidade que deseja adicionar: "))
            break
        except ValueError:
            print("-----------------------------------")
            print("Número inválido! Tente novamente")
            print("-----------------------------------")
    d.cadastros[ind-1]["qtd"] = d.cadastros[ind-1]["qtd"] + n
    print("Livros adicionados com sucesso!")