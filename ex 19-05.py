#1
def n_imp(valor):
    n = []
    for i in range(1, valor + 1):
        if i % 2 != 0:
            n.append(i)
    return print(*n)

#2
def n_multi3e5(valor):
    n = []
    for i in range(1, valor + 1):
        if i % 3 == 0 and i % 5 == 0:
            n.append(i)
    return print(*n)

#3
def som_matriz(matrix):
    soma = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])): 
            if x != y and x >= y + 1: 
                soma += matrix[y][x]
    return soma    

#matriz pra teste
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

n_imp(100)
n_multi3e5(100)
print(som_matriz(matriz))