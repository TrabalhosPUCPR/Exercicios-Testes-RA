while True:
    esc = input("Digite o numero do exercicio: ")

    """
    Escreva uma função que receba uma lista com números e retorne uma lista
    com as raízes dos números fornecidos como entrada
    """
    if esc == "1":
        def lista_raiz(lista):
            lista_raizes=[]
            for i in range(len(lista)):
                lista_raizes.append(lista[i]**(1/2))
            return lista_raizes

        lista = int(input("Digite o numero onde a lista comeca: ")) 
        listafim = int(input("Digite o numero onde a lista termina: ")) 

        print(lista(range(lista, listafim+1)))

    """
    Escreva uma função que calcule o fatorial de um número n positivo
    qualquer
    """
    if esc == "2":
        def  fatorial(fat):
            f = 1
            for x in range(1, fat):
                f *= fat
                fat -= 1   
            return f
        fat = int(input("Digite o fatorial: ")) 
        print(fatorial(fat))

    """
    Escreva um algoritmo que receba dois valores n e m que representem o
    número de linhas e colunas de uma matriz e a instancie. Ainda, cada
    posição da matriz deve ser calculada por i2 + j3, sendo que i e j representam
    os índices das linhas e colunas, respectivamente. Finalmente, apresente a
    soma dos valores para cada coluna.
    """
    import random as rdm
    if esc == "3":
        def criar_matriz(n, m):
            matriz = []
            matriz2 = []
            for y in range(n):
                matriz.append([])
                matriz2.append([])
                for x in range(m):
                    matriz[y].append(rdm.randint(0, 5))
                    matriz2[y].append(y**2 + x**3)
            return matriz, matriz2

        def printMatriz(matriz):
            for y in range(len(matriz)):
                for x in range(len(matriz[y])):
                    print("|", end="")
                    print(matriz[y][x], end="")
                print("|")

        def soma_matriz(matriz):
            soma = 0
            for y in range(len(matriz)):
                for x in range(len(matriz[y])):
                    soma += matriz[y][x]
            return soma

        n = int(input("Digite o numero de linhas: "))
        m = int(input("Digite o numero de colunas: "))
        
        matriz, matriz2 = (criar_matriz(n, m))
        printMatriz(matriz)
        print("O de baixo e linha^2 + coluna^3")
        printMatriz(matriz2)
        print("A partir daqui e a soma de tudo")
        print(soma_matriz(matriz))
        print("O de baixo e linha^2 + coluna^3")
        print(soma_matriz(matriz2))

    """
    Escreva uma função que receba uma lista de números e retorne quantos
    números ímpares, pares, nulos, positivos e negativos existem nela.
    """
    if esc == "4":
        def tudo(lista):
            impar, par, nulo, positivo, negativo = 0,0,0,0,0
            for i in lista:
                if i % 2 == 0:
                    par += 1
                else:
                    impar += 1
                if i >= 0:
                    positivo += 1
                    if i == 0:
                        nulo += 1
                else:
                    negativo += 1
            return impar, par, nulo, positivo, negativo
                
        lista = int(input("Digite o numero onde a lista comeca: ")) 
        listafim = int(input("Digite o numero onde a lista termina: ")) 
        resultado = tudo(range(lista, listafim+1))
        print(f'Quantidade de numeros: Impar {resultado[0]}, Par {resultado[1]}, Nulo {resultado[2]}, Positivo {resultado[3]}, Negativo {resultado[4]}')




