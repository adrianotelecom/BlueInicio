#for cout in range(1,61,2):
    #print(cout)



"""
cont = -1
while cont <58:
    cont+=2
    print(cont)"""



"""
cont = 0
while cont < 60:
    if cont % 2 != 0:
        print(cont)
    cont += 1"""


opc = 1
while opc == 1:
    num = 1
    cont = 1
    numeros = []
    numeros_solicitados = int(input('Quantos numeros impares você deseja: '))

    while cont <= numeros_solicitados:
        numeros.append(num)
        num += 2
        cont += 1

    print(f'O tamanho da lista de numeros impares é: {len(numeros)}')
    print(numeros)
    
    resp = input('Deseja continuar [S/N]:').upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida')
        resp = input('Deseja continuar [S/N]:').upper()
    while resp == 'N':
        print('Fim do programa')
        opc = 0
        resp = ""

