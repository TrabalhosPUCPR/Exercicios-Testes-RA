import time

#questao 1
print("QUESTAO 1")
print("\n")
time.sleep(2)
ladoa = float(input('insira o valor do primeiro lado'))
ladob = float(input('insira o valor do segundo lado'))
ladoc = float(input('insira o valor do terceiro lado'))

if(ladoa > 0) and (ladob > 0) and (ladoc > 0) and (ladoa < (ladob + ladoc)) and (ladob < (ladoa + ladoc)) and (ladoc < (ladob + ladoa)):
    if(ladoa == ladob) or (ladoa == ladoc) or (ladoc == ladob):
        if(ladoa == ladob) and (ladoa == ladoc):
            print('e um triangulo equilatero')
        else:
            print('e um triangulo isosceles')

    if(ladoa != ladob) and (ladoa != ladoc) and (ladob != ladoc):
        print('e um triangulo escaleno')
else:
    print('nao forma um triangulo')


time.sleep(2)
# questao 2
print("\n")
print("QUESTAO 2")
print("\n")
numero = int(input("Digite um numero inteiro qualquer:"))
if(numero==5):
    print("e igual a 5")
else:
    if(numero==20):
        print("e igual a 20")
    else:
        if(numero==400):
            print("e igual a 400")
if(numero>500 and numero<1000):
    print("esta entre 500 e 1000")
else:
    print("Nao esta entre 500 e 1000")


time.sleep(2)
#questao 3
print("\n")
print("QUESTAO 3")
print("\n")
import numpy as np

#delta = (b**2) -4*a*c
#x = (-b + sqrt(delta))/(2*a)

a = int(input('Digite o valor de A '))
b = int(input('Digite o valor de B '))
c = int(input('Digite o valor de C '))

if(a == 0):
    print('nao da, A = 0')
else:
    delta = (b**2) -4*a*c
    if(delta >= 0):
        x1 = (-b + np.sqrt(delta))/(2*a)
        x2 = (-b - np.sqrt(delta))/(2*a)
        if(delta > 0):
            print('S = {x e R / x = ',x2, 'e x = ',x1,'}')
        else:
            print('Raiz unica = ', x2)
    else:
        print('nao existe solucao real')


