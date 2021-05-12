filmes = ["Os vingadoeres", "HP", "Forrest Gump", "A Procura da Felicidade", "Como eu era antes de voce","O lobo de",]
print(filmes)
filmes.append("Power Rangers") #Adicionar outro filme e ele vai ir para o final da lista
print(filmes)
print()
a = input("Digite um filme: ") # para o usuario adicionar um filme com um espaço ele dara o estaso entre a pergunta
filmes.append(a)
print(filmes)
print()
filmes_novos = ["historia Cruzadas", "Esquereceram de mim","Desventiras em Série", "Poderoso Chefão","De Volta para o futuro", "Ben hur"]
filmes.extend(filmes_novos)# a expressão para juntas as listas (.extrend)
print(filmes)
print()
print(filmes)
filmes.sort() #Ordenar a lista em ordem alfabetica serve para numeros e string
print(filmes)
print()
filmes.reverse() #Colocar ao contrario de tras pra frente de Z a A
print()
filmes.insert(1,"Pianista")#posisão onde quelo colocar determinado obejto(filme)
print(filmes)
print()
filmes.insert(10,"Projeto X")#posisão onde quero colocar determinado obejto(filme)
print(filmes)
print()
filmes.remove("HP")#remover um filme da lista
print()
print(filmes)
print()
filmes.pop(7)#remover um filme da lista pela posição
filmes.pop()
filmes.pop()#(.opp() vazio ele ira apagar o ultimo filme)
del filmes[1]#deletar na posição indicada = colocando(del filmes [:]apagara tudo) = del filmes[0:3] ele ira apagar um elemento a menos no caso de o 0,1,2.
print()
for filme in filmes: #colocar os filmes em lista um embaixo do outro
    print( filme)
    print()
print(len(filmes))#ver o tamnho da lista de filmes a quantidade de filmes

