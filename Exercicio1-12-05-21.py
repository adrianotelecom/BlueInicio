#Exercício 1  - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparecem as vogais a,e,i,o,u
frase = input("Digite uma frase: ")
vogais = 0
espacos = 0
for letra in frase:
    if letra == "":
        espacos += 1
    elif letra in "aeiou":
        vogais += 1
print(frase)
print()
print("Esta e a quantidade de caracteres da sua frase: ")
print(len(frase))
print()
print("Esta e a quantidade de vogais da sua frase: %d" %(vogais))
print()
   






