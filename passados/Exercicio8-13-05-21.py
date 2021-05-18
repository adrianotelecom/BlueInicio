#8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#○ “Telefonou para a vítima?”
#○ “Esteve no local do crime?”
#○ “Mora perto da vítima?”
#○ “Devia para a vítima?”
#○ “Já trabalhou com a vítima?”
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino”. Caso contrário, ele será classificado como “Inocente”.

val = []
val.append(input("Telefonou para a vítima? 1-Sim ou 0-Não: "))
print()
val.append(input("Esteve no local do crime? 1-Sim ou 0-Não: "))
print()
val.append(input("Mora perto da vítima? 1-Sim ou 0-Não: "))
print()
val.append(input("Devia para a vítima? 1-Sim ou 0-Não: "))
print()
val.append(input("Já trabalhou com a vítima? 1-Sim ou 0-Não: "))
print()
soma_Crime = 0
for i in val: 
  soma_Crime += int(i)
if (soma_Crime < 2):
 print("\nInocente")
elif (soma_Crime == 2):
 print("\nSuspeita")
elif (3 <= soma_Crime <= 4):
 print("\nCúmplice")
elif (soma_Crime == 5):
 print("\nAssassino")
 print()