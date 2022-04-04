"""

exercicio 1

Escreva um algoritmo que leia um vetor com 4 valores e apresente
sua média

"""

vetor = [7,8, 9, 10]
print(f'Exercicio 1: {sum(vetor)/len(vetor)}')

"""

exercicio 2

Escreva um algoritmo que instancie uma matriz de ordem 4x4 e
imprima sua diagonal principal

"""

resultado = []
resultado2 = []
vetor = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
inverso = len(vetor) - 1
print("exercicio 2: ", end = '')
for i in range(len(vetor)):
    resultado.append(vetor[i][i])
    resultado2.append(vetor[inverso][i])
    inverso -= 1
resultado2.reverse()
print(f'{resultado} ', end = '')
print(f'{resultado2} ', end = '')

"""

exercicio 3

Escreva um algoritmo que instancia uma lista de tamanho 5 e
imprima seus valores seguido da soma destes valores

"""

print("\nexercicio 3: ", end = '')
vetor = range(1, 6)
for i in range(len(vetor)):
    print(f'{vetor[i]} ', end = '')
print("     Soma: ", sum(vetor))

"""

exercicio 4

Escreva um algoritmo que receba uma matriz de ordem 3x3 e
imprima seus valores seguido da soma destes valores

"""
vetor = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultado = 0
i = 0
i2 = 0

print("exercicio 4: ", end = '')
col = len(vetor)
mat = len(vetor[0]) * col       #daria pra usar numpy.size(vetor) ao inves de fazer esses calculo pra pega o tamanho de um array de 2 dimensoes
while mat > 0:
    resultado += vetor[i2][i]
    print(f'{vetor[i2][i]} ', end = '')
    mat -= 1
    i += 1
    if i == 3:
        i2 += 1
        i = 0

print(f'    Soma: {resultado} ', end = '')

"""

exercicio 5

Escreva um programa em Python capaz de calcular e imprimir na tela a
série de Fibonacci até o vigésimo termo. A série de Fibonacci é formada
pela seguinte sequência: 1, 1, 2, 3, 5, 8, 13, 21, .... 

"""

print("\nExercicio 5: ", end = '')
F = [1, 1]
x = 0

for i in range(20):
    if (i >= 2):
        F.append(F[i-1]+F[i-2])
    print(f'{F[i]} ', end = '')

"""

exercicio 6

Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto
Felisberto tem 1,10 metro e cresce 3 centímetros por ano. Construa um
algoritmo em Python que calcule e mostre quantos anos serão
necessários para que Felisberto seja maior que Anacleto.

"""

a = 1.50
f = 1.10
ano = 0

while f < a:
    a +=0.02
    f += 0.03
    ano += 1
print(f'\nExercicio 6: Felisberto sera maior que Anacleto no {ano}⁰ ano com {round(f, 4)} metros e Anacleto com {round(a, 4)} metros')

"""

exercicio 7

Em um restaurante que vende comida por quilo, o gerente resolveu
avaliar quanto as pessoas costumam comer. Para isso, o gerente te
contratou para desenvolver um programa em Python para calcular o valor
médio, em quilos, de um prato. Assim, seu programa deve permitir a
entrada do peso de cada prato (serão N no total) e imprimir na tela o peso
médio. O programa deve também imprimir quantos pratos tem peso maior
que 800 gramas.

"""

prato = []
peso = float(input("Exercicio 7: Digite o peso para adicionar ao primeiro prato: "))
ver = str

while ver != "n":
    prato.append(peso)
    ver = str(input("Digite o peso para adicionar ao prato ('n' para calcular a media): "))
    if ver == "n":
        peso = sum(prato)/len(prato)
    else:
        peso = float(ver)

for i in range(len(prato)):
    if prato[i]*1000 > 800:
        print(f'O prato {i+1} tem mais que 800 gramas, ele tem {prato[i]*1000} gramas')

print(f'A media do peso dos pratos e: {peso}')

"""

exercicio 8

Implemente um algoritmo que imprima o somatório dos 10 primeiros
números naturais a partir do 1

"""

n = 0

for i in range(10):
    n += 1
print("Exercicio 8: ", n) 

"""

exercicio 9

Implemente um algoritmo que recebe como entrada a nota de um
estudante na disciplina. Repita este processo enquanto a nota for
inválida.

"""

nota = float(input("Digite uma nota de 0 a 10: "))

while nota > 10 or nota < 0:
    nota = float(input("Digite uma nota ENTRE OS NUMEROS 0 E 10: "))

print("Exercicio 9: ", nota)