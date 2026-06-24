import unicodedata

def xy(): 
    for i in range(1,16):
        if i%5 == 0 and i%3 == 0:
           print('XY', end=' ')
        elif i%5 == 0:
           print('Y', end=' ')
        elif  i%3 == 0:
           print('X', end=' ')
        else:
            print(f'{i}', end=' ')


def percorrer():
    n = int(input('Digite um valor: '))
    if n < 1:
        print("numero invalido")
        return
    
    for i in range(1,n+1):
        if i%7 == 0:
            print('Multiplo de 7 encontrado!')
            return
        elif i%2 != 0:
            print(i)


def impares():
    q, t = 0, 0
    for i in range(1,31):
        if i%2 != 0:
            print(i, end=' ')
            q+=1
            t+=i
    print(f'\nNumeros exibidos: {q}\nSoma total: {t}')


def tabuada():
    n = int(input('Digite um valor: '))
    if n < 1:
        print("numero invalido")
        return
    
    for i in range(1,11):
        r = n * i
        if r > 20:
            print(f'| {n} X {i:2d} = {r:3d} |')

    
def soma():
    n = int(input('Digite um valor: '))
    if n < 1:
        print("numero invalido")
        return
    
    s = 0
    for i in range(1,n+1):
        if i%3 != 0:
            s+=i
            if s > 100 or i == n:
                print(f'Soma: {s}')
                return


def percorrer2():
    q = 0
    for i in range(4,61):
        if i%8 != 0 and i%4 == 0:
            q+=1
            print(i, end=' ')
    print(f'\nNumeros exibidos: {q}')


def soma5():
    s, q, inv = 0, 0, 0
    for i in range(5):
        while True:
            n = int(input('Digite um valor: '))
            if n >= 0:
                break
            print("numero invalido")
            inv+=1
        s+=n
        q+=1
    print(f'Soma: {s}\nMedia: {s/q:.1f}\nIgnorados: {inv}')


def desenho():
    for i in range(7):
        if i == 0 or i == 6:
            print(' --------- ')
        else:
            for f in range(7):
                if f == 0 or f == 6:
                    print(' | ',end='')
                elif f < i:
                    print(end=' ')
                else:
                    print('*',end='')
            print('')


def string():
    s = "Programação"
    for i in range(len(s)):
        if unicodedata.normalize('NFD', s[i]).encode('ascii', 'ignore').decode('utf-8') not in ('a','e','i','o','u'):
            tipo = 'Consoante'
        else:
            tipo = 'Vogal'
        print(f'Indice: {i:2d} - Letra: {s[i]} - Tipo: {tipo}')


def percorrer3():
    n = int(input('Digite um valor: '))
    if n < 2:
        print("numero invalido")
        return
    
    q,t = 0,0
    for i in range(2,n+1):
        div = 0
        for f in range(2,i):
            if i%f == 0:  
                div+=1
        if div == 0:
            print(i, end=' ')
            q+=1
            t+=i 
    print(f'\nQuantidade: {q} \nSoma: {t}')





percorrer3()
