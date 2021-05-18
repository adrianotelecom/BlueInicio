#Desafio 1 - Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.
#Exemplo: 3025 = 55 e 55**2 é igual á 3025

for n in range(1000,10000):
    n1 = n //100
    n2 = n % 100
    if (n1+n2)**2 == n:
        print(n)