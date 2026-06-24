
def nota():
    alunos = {}
    aprovados = []
    reprovados = []

    print('cadastre os alunos')
    while(len(alunos) < 5):
        nome = input('nome: ')
        nota = float(input('nota: '))
        
        if nome != '':
            alunos[nome] = round(nota,1)
        else:
            print('valores invalidos')

    print('Cadastrados:\n', alunos)

    for aluno, nota in alunos.items():
        if nota >= 6:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)
    
    print('Aprovados: ', aprovados)
    print('Reprovados: ' , reprovados)



def produtos():
    produtos = {}
    while(True):
        produto = input('produto: ')
        if produto == 'fim': break 

        preco = input('preço: ')
        if preco == 'fim': break

        produtos[produto] = float(preco)
        print('cadastro realizado')
    
    print('cadastros encerrados')
    print('\nprodutos cadastrados:')

    soma = 0
    for i, p in produtos.items():
        soma += p
        print(f'- {i} R$ {p}')


    
    print(f'\nmais caro: {max(produtos.values()):.2f}')
    print(f'media: R$ {soma/len(produtos):.2f}')



def frase():
    frase = input('frase: ')
    frase = frase.lower().replace(' ','_')
    
    print(frase.upper())
    print(frase)
    print(f'quantidade de vogais: {frase.count('a')+
                                   frase.count('e')+
                                   frase.count('i')+
                                   frase.count('o')+
                                   frase.count('u')}')
    print(f'quantidade de A: {frase.count('a')}')
    if 'python' in frase:
        print('possui python')
    else:
        print('não possui python')



def mercado():
    produtos = []

    while True:
        produto = input('produto: ')
        if produto == 'fim':
            while True:
                print(f'cadastros({len(produtos)}): {produtos}')
                rm = input('remover: ')
                if rm in produtos:
                    produtos.remove(rm)
                    print('removido com sucesso')
                else:
                    print('produto não encontrado')

        produtos.append(produto)
        print('cadastro realizado')



def votos():
    candidatos = {'ana': 0, 'bruno': 0, 'carla': 0}

    vt_inv = 0
    while True:
        vt = input('nome do candidato: ')
        if vt == 'fim': break
        elif vt in candidatos:
            candidatos[vt] += 1
        else:
            vt_inv += 1

    print(f'\nresultado: {candidatos}')
    print(f'votos invalidos: {vt_inv}')

    if list(candidatos.values()).count(max(candidatos.values())) == 1:
        print(f'vencedor: {max(candidatos, key=candidatos.get)}')
    else: 
        print('empate')



def funcionario():
    funcionario = {'nome': 'Lucas', 
                   'cargo': 'Analista', 
                   'salario': 3500.0}
    print(funcionario)
    funcionario['salario'] = 4000.0
    funcionario['departamento'] = 'TI'
    print(funcionario)



def vogais():
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    frase = input('frase: ').lower()

    for vg in vogais:
        vogais[vg] = frase.count(vg)

    print(vogais)


def capitais():
    capitais = {
        'São Paulo': 'São Paulo',
        'Rio de Janeiro': 'Rio de Janeiro',
        'Minas Gerais': 'Belo Horizonte',
        'Bahia': 'Salvador',
        'Paraná': 'Curitiba'
    }

    for estado, capital in capitais.items():
        print(f'A capital de {estado} é {capital}.')



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
        


def votos2():
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

    if list(candidatos.values()).count(max(candidatos.values())) == 1:
        print(f'vencedor: {max(candidatos, key=candidatos.get)}')
    else: 
        print('empate')
    print(candidatos)


votos2()