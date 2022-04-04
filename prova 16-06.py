"""A função descrita abaixo objetiva retornar o somatório de todos os valores positivos, isto é, 
maiores que zero, fornecidos como parâmetro em uma lista. 
Infelizmente, o programador cometeu um ou mais erros nesta função e ela deve ser corrigida. 
Desta forma, seu objetivo é reescrever esta função no espaço fornecido abaixo, corrigindo a função para que ela funcione de forma adequada.
 
Código original

def soma_positivos(lista):

    soma = 1

    for i in range(len(lista) + 1):

        if lista[i] > 0:

            soma = lista[i]   

"""
listaa = [3, 4, 3, 13, 2.5]

def soma_positivos(lista):
    soma = 0
    for i in lista:
        if i > 0:
            soma += i  
    return soma

print("1:", soma_positivos(listaa))


"""
Um programador foi incumbido de desenvolver uma função que recebe como parâmetro 
uma lista de valores inteiros (tipo int) e que retornasse outra lista 
com o dobro dos valores pares e o triplo dos valores ímpares existentes na lista original. 
Infelizmente, o programador não terminou a função e você deve completá-la abaixo:

Código a ser completado

def dobro_triplo(lista):

    l_ret = []

    for i in range(___________):

        if l[i] % 2 == 0:

            l_ret.append(2 * lista[i])

            ___________________:

            l_ret.append(3 * lista[i])

    return l_ret
"""
def dobro_triplo(lista):
    l_ret = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            l_ret.append(2 * lista[i])
        else:
            l_ret.append(3 * lista[i])
    return l_ret

print("2:", *dobro_triplo(listaa))

"""
A série de Fibonacci é formada pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc. Nesta sequência, cada termo é definido pela soma dos dois anteriores. 
Um programador tentou escrever uma função que retornasse até a n-ésima posição desta sequência, contudo, o código não funciona de forma apropriada. 
Seu objetivo é corrigir esta função no espaço fornecido abaixo. 

Dicas: (i) Lembre-se de verificar valores pequenos de n. 
(ii) Verifique laços de repetição infinitos.
(iii) Use teste de mesa para verificar a função abaixo passo a passo.

Código original

def fibonacci(n):

    a = 0

    b = 1

    fib_vals = [a,b]

    while fib_vals != n:

        soma = a + b

        fib_vals.append(soma)

        b = soma

        a = b

    return fib_vals
"""
def fibonacci(n):
    contador = 2
    fib_vals = [0, 1]
    if n > 1:
        while contador != n:
            soma = fib_vals[-2] + fib_vals[-1]
            fib_vals.append(soma)
            contador += 1
        return fib_vals
    else:
        return fib_vals[0]

print("3:", fibonacci(1))

"""
Um programador foi incumbido de escrever uma função chamada aloca_matriz que, a partir de dois parâmetros n e m, aloque uma matriz usando listas em Python com n linhas e m colunas e que instanciasse seus valores como uma matriz identidade. Lembre-se: uma matriz identidade é aquela cuja diagonal principal possui valores 1.0 (um) e os demais valores são 0.0 (zero). O código criado pelo programador está abaixo, contudo, ele está incorreto. Seu objetivo é então corrigir este código para garantir que seu funcionamento seja correto e que nenhuma matriz seja retornada caso os valores de n e m sejam inválidos (retorne Null neste caso).

Código original

def aloca_linha(m):

  return m + 1 * [0]

def aloca_matriz(n, m):

  mat = []

  for i in range(n):

    mat.append(aloca_linha(m))

  return mat

m = aloca_matriz(5,2)

print(m)
"""

def aloca_linha(i, z):
    if i == z:
        return 1
    else:
        return 0

def aloca_matriz(n, m):
    if n <= 0 or m <= 0:
        print("Valor inserido invalido")
        return None
    else:
        mat = []
        for i in range(n): #loop para toda linha
            mat.append([])
            for z in range(m): #loop para toda coluna
                mat[i].append(aloca_linha(i, z))
        return mat

m = aloca_matriz(0,10)
print(m)