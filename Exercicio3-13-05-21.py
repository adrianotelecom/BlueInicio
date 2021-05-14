#3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e mostre ao final a quantidade de pessoas de cada estado civil. 
s = 0
c = 0

for count in range(15):
    estado_civil = input("Digite seu estado civil (s ou c):  ").upper()
    if estado_civil =='S':
        s = s + 1
    else:
        c = c + 1

print("solteiros: {} e casado: {}" .format(s,c))