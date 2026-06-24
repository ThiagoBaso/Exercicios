def semana():
    semana = []

    while len(semana) < 7:
        semana.append(input("Digite o dia da Semana: "))

    print(f'Lista: {semana}')



def contar_sete():
    numeros = [4, 7, 2, 7, 9, 3, 7, 1] 

    quantidade = numeros.count(7)

    print(f"Lista: {numeros}")
    print(f"O numero 7 aparece {quantidade} vez(es).")



def remover_aluno():
    alunos = ["Thiago", "Bruno", "Luis", "Diego", "Pedro"]

    print(f"Lista de alunos: {alunos}")
    nome = input("Digite o nome do aluno que deseja remover: ")

    if nome in alunos:
        alunos.remove(nome)
        print(f"Aluno removido com sucesso.")
        print(f"Lista atualizada: {alunos}")
    else:
        print("O nome informado nao existe na lista.")



def limpar_lista():
    numeros = []

    for i in range(1, 11):
        numeros.append(i)

    print(f"Lista antes do clear: {numeros}")

    numeros.clear()

    print(f"Lista depois do clear: {numeros}")



def contar_letras():
    letras = ['a', 'b', 'a', 'c', 'a', 'd', 'b', 'a']

    quantidade_a = letras.count('a')
    quantidade_b = letras.count('b')

    print(f"Lista: {letras}")
    print(f"A letra 'a' aparece {quantidade_a} vez(es).")
    print(f"A letra 'b' aparece {quantidade_b} vez(es).")

    if quantidade_a > quantidade_b:
        print("A letra 'a' possui mais ocorrencias.")
    elif quantidade_b > quantidade_a:
        print("A letra 'b' possui mais ocorrencias.")
    else:
        print("As duas letras aparecem a mesma quantidade de vezes.")



def cadastrar_alunos():
    alunos = []

    while True:
        nome = input("Digite o nome do aluno ou 'fim' para encerrar: ")

        if nome.lower() == 'fim':
            break

        alunos.append(nome)

    print(f"Lista de alunos cadastrados: {alunos}")

    nome_remover = input("Digite o nome do aluno que deseja remover: ")

    if nome_remover in alunos:
        alunos.remove(nome_remover)
        print("Aluno removido com sucesso.")
        print(f"Lista atualizada: {alunos}")
    else:
        print("O nome informado nao existe na lista.")



def carrinho_compras():
    carrinho = ['leite', 'pão', 'queijo', 'manteiga']

    print(f"Carrinho inicial: {carrinho}")

    carrinho.remove('pão')
    print(f"Carrinho apos remover 'pão': {carrinho}")

    carrinho.append('café')
    print(f"Carrinho apos adicionar 'café': {carrinho}")


def contar_primeiro_numero():
    numeros = []

    while len(numeros) < 8:
        try:
            numero = int(input(f"Digite o {len(numeros) + 1} numero inteiro: "))
        except ValueError:
            print("Digite apenas numeros inteiros.")
            continue

        numeros.append(numero)

    primeiro_numero = numeros[0]
    quantidade = numeros.count(primeiro_numero)

    print(f"Lista: {numeros}")
    print(f"O primeiro numero digitado foi {primeiro_numero}.")
    print(f"Ele aparece {quantidade} vez(es) na lista.")



def lista_compras():
    itens = []

    while True:
        item = input("Digite um item ou 'sair' para encerrar: ")

        if item.lower() == 'sair':
            break

        itens.append(item)

    print(f"Itens cadastrados: {itens}")

    itens.clear()

    print(f"Lista apos clear: {itens}")
    print(f"Quantidade de itens na lista: {len(itens)}")



def contar_cores():
    cores = ['azul', 'verde', 'azul', 'vermelho', 'azul', 'verde']
    cores_contadas = []

    print(f"Lista de cores: {cores}")

    for cor in cores:
        if cor not in cores_contadas:
            quantidade = cores.count(cor)
            print(f"A cor {cor} aparece {quantidade} vez(es).")
            cores_contadas.append(cor)



def gerenciar_contatos():
    contatos = []

    while True:
        print("\n1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Quantas vezes um nome aparece")
        print("4 - Limpar todos os contatos")
        print("5 - Exibir lista de contatos")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        match opcao:
            case "1":
                nome = input("Digite o nome do contato: ")
                contatos.append(nome)
                print("Contato adicionado com sucesso.")

            case "2":
                nome = input("Digite o nome do contato que deseja remover: ")
                if nome in contatos:
                    contatos.remove(nome)
                    print("Contato removido com sucesso.")
                else:
                    print("O contato informado nao esta na lista.")

            case "3":
                nome = input("Digite o nome que deseja contar: ")
                quantidade = contatos.count(nome)
                print(f"O nome {nome} aparece {quantidade} vez(es) na lista.")

            case "4":
                contatos.clear()
                print("Todos os contatos foram removidos.")

            case "5":
                print(f"Lista de contatos: {contatos}")

            case "0":
                print("Programa encerrado.")
                break

            case _:
                print("Opcao invalida. Tente novamente.")
