def carro():
    carro = {}

    carro["marca"] = input("Informe a marca do carro: ")
    carro["modelo"] = input("Informe a modelo do carro: ")
    carro["ano"] = input("Informe a ano do carro: ")
    carro["cor"] = input("Informe a cor do carro: ")

    print(f'\nMarca: {carro["marca"]}\nModelo: {carro["modelo"]}\nAno: {carro["ano"]}\nCor: {carro["cor"]}')



def estoque():
    estoque = {
        'arroz': 50,
        'feijão': 30,
        'macarrão': 45
    }
    print(f'quantidade de feijão: {estoque["feijão"]}')

    estoque["azeite"] = 20
    print(f"estoque atualizado:\n{estoque}")



def usuario():
    user = {}

    user["nome"] = input("Informe o nome: ")
    user["idade"] = input("Informe a idade: ")
    user["cidade"] = input("Informe cidade: ")

    print(f'\nNome: {user['nome']}\nIdade: {user['idade']}\nCidade: {user["cidade"]}')



def notas():
    notas = {
        'Matemática': 8.5,
        'Português': 7.0,
        'Ciências': 9.0,
        'História': 6.5
    }
    soma = 0 

    for i in notas.items():
        print(f'{i[0]} - {i[1]}')
        soma+=i[1]

    print(f'Media: {soma/len(notas):.2f}')



def dicionario():
    dicionario = {
        'gato': 'cat',
        'cachorro': 'dog',
        'casa': 'house',
        'carro': 'car',
        'livro': 'book'
    }

    palavra = input('Palavra em Portugues: ')

    if palavra in dicionario:
        print(f'Tradução: {dicionario[palavra]}')
    else:
        print('palavra não encontrada"')



def funcionario():
    funcionario = {
        'nome': 'Lucas',
        'cargo': 'Analista',
        'salario': 3500.0
    }

    funcionario['salario'] = 4000.0
    funcionario['departamento'] = 'TI'

    print(funcionario)



def frases():
    frase = input('Digite a frase: ')
    vogais = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    } 

    for i in frase:
        if i in vogais:
            vogais[i] += 1

    print(vogais)



def capitais():
    capitais = {
        "Sao Paulo": "Sao Paulo",
        "Rio de Janeiro": "Rio de Janeiro",
        "Minas Gerais": "Belo Horizonte",
        "Bahia": "Salvador",
        "Parana": "Curitiba"
    }

    for estado, capital in capitais.items():
        print(f"A capital de {estado} é {capital}")



def alunos():
    N = int(input('Numero de alunos a ser inserido: '))
    alunos = {}

    for i in range(N):
        nome = input('Nome: ')
        alunos[nome] = float(input('Nota: '))

    print("Aprovados:")
    for aluno, nota in alunos.items():
        if nota >= 6:
            print(aluno)



def inventario():
    inventario = {
        'espada': 2,
        'escudo': 1,
        'poção': 5,
        'flecha': 30,
        'armadura': 1
    }
    qtd_total = 0

    print('Itens com + de 2 no Inventario: ')
    for item, qtd in inventario.items():
        qtd_total += qtd
        if qtd >= 2:
            print(f' - {item}')
        


def votos():
    candidatos = {
        "Ana": 0,
        "Bruno": 0,
        "Carlos": 0
    }

    while(True):
        voto = input("Seu voto (ou 'fim' para encerrar.): ") 

        match voto:
            case 'Ana':
                candidatos['Ana'] += 1
            case 'Bruno':
                candidatos['Bruno'] += 1
            case 'Carlos':
                candidatos['Carlos'] += 1
            case 'fim':
                break
            case _:
                print("Candidato inválido")

    vencedor = max(candidatos, key=candidatos.get)
    print(f'Vencedor: {vencedor} - {candidatos[vencedor]} votos')



votos()
