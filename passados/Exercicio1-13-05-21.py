#1. Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

tabuada=int(input("Digite um numero para Criar a tabuada: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )