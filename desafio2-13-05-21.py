#Desafio 2 - Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista. Ao final, seu script deverá fornecer a média geral do aluno.


materias=int(input('Digite a quantodade de materias cursadas: '))
notas=[]

for cont in range(materias):
    nota=float(input(f'Digite a nota da materia informada {cont+1}?:'))
    notas.append(nota)

print(f'{(sum(notas)/materias):.2f}')

