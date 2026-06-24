def planetas():
    planetas = ('Mercurio', 'Venus', 'Terra', 'Marte')
    print(f'Primeiro: {planetas[0]}')
    print(f'Ultimo: {planetas[-1]}')
    print(f'Total: {len(planetas)}')


def notas():
    notas = (7.5, 8.0, 6.5, 9.5, 7.0)
    i=1
    for nota in notas:
        print(f'Nota {i}: {nota}') 
        i+=1
    print(f'Quantidade de notas: {len(notas)}')


def numeros():
    numeros = (3, 8, 1, 15, 7, 4, 12)
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    print(f'Maior numero: {maior}')


def cores():
    cores = ('vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta')
    for i in range(len(cores)):
        print(f'Posição no Arco-Iris: {i+1} - Cor: {cores[i]}')


def valores():
    valores = (10, 25, 10, 30, 10, 5, 10)
    qtd = 0
    for valor in valores:
        if valor == 10:
            qtd+=1
    print(f'O Valor 10 aparece {qtd} vezes!')       


def dados():
    dados = (('Ana', 8.5), ('Bruno', 7.0), ('Carla', 9.0))
    total = 0
    for dado in dados:
        print(f'{dado[0]} -> {dado[1]}')
        total+=dado[1]
    print(f'Media: {total/len(dados):.2f}')


def meses():
    meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','desenbro')
    mes = int(input("escola um mes(1 a 12): "))
    if mes < 1 or mes > 12:
        print('Numero Invalido!')
        return
    print(f'Mes {mes} -> {meses[mes-1]}')


def temperatura():
    temperaturas = (28.4, 31.1, 26.7, 29.3, 33.5, 25.0)
    soma = 0
    for temp in temperaturas:
        soma+=temp
    media = soma/len(temperaturas)
    qtdMaior = sum(x > media for x in temperaturas)
    print(f'Media: {media:.2f}\nAcima da media: {qtdMaior}')


def produto():
    produtos = ('notebook', 'mouse', 'teclado', 'monitor', 'headset')
    item = input('Informe o produto que deseja consultar: ')
    if item in produtos:
        print('Item encontrado, esta disponivel!')
    else:
        print('Item não encontrado!')


def letras():
    letras = ('p', 'y', 't', 'h', 'o', 'n')
    for i in range(len(letras)):
        print(f'Letra: {letras[-1-i]}')


def alunos():
    alunos = ( ('Maria', 8.5, 22), ('João', 5.5, 20),('Fernanda', 9.0, 21), ('Carlos', 6.0, 23), ('Beatriz', 4.5, 19))
    maior = ['',0]
    somaNota = 0
    somaIdade = 0
    print('Aprovados: ', end='')
    for aluno in alunos:
        if aluno[1] > 6.0:
            print(aluno[0], end=', ')
        if aluno[1] > maior[1]:
            maior[0] = aluno[0]
            maior[1] = aluno[1]
        somaNota+=aluno[1]
        somaIdade+=aluno[2]
    print(f'\nMaior nota: {maior[0]} -> {maior[1]}')
    print(f'Media de notas: {somaNota/len(alunos):.2f}')
    print(f'Media de idades: {somaIdade/len(alunos):.0f}')
        
