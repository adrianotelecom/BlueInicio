contatos_lista = [("Gustova", '1234-5678'), ("Paulo", '9999-8888'), ("Jaque",'8765-3456'), ("Laura","7788-8877")]
print(contatos_lista[2][1])

zoo = (("Zona1","Girafa"),("Zona2","Ihama"))

# Para criar dicionários utiliza-se {} ou a função dict ()
# Para lista usamos []

teste = dict(zoo)
print(teste)

contatos = dict(contatos_lista)
print(contatos)
print()
print(contatos["Jaque"])
print()
#Método get -> buscar valores em dicionários pela key (chave)

print(contatos.get("Chuck Norris", "Contato não encontrado"))
print()
print(contatos.get("Jaque", "Contato não encontrado"))
print()
#Método Values -> buscar valores em um dicionario (retorna True / False)
print("7788-8877" in contatos.values())
print()
print("7788-8897" in contatos.values())
print("=-="*60)
print("Adicionando Contados no dicionario.")
print()
contatos  ["mulher Maravilha"] = "2233-9665"
contatos  ["Deadpool"] = "666"
print(contatos)
print()
# Adicionando com input - Forma 1 
a = input("Digite o valor da chave: ")
b = input("Digite o valor: ")
contatos[a]=b
print(contatos)
print()
#Adicionando com input - Forma 
contatos [input("digite o nome: ")] = input("digite o telefone: ")
print(contatos)
print()


print("*/*"*50)
print("Removendo Contados no dicionario")
print("$"*120)
print()

del contatos ["mulher Maravilha"]
print(contatos)

print(contatos.pop("Deadpool", "Contato não encontrado"))
print(contatos.pop("Thor", "Contato não encontrado"))
print()


contatos.clear() #Limpa tudo
print(contatos)

print("*/*"*50)
print("Unindo Dicionários")
print("--"*80)
print()

contatos_matheus = [("Yago","1234-5679"),("Maicon","9999-8887"),("Thiago","8765-3455"),("Gabriel","7788-8876")]
contatos2 = dict(contatos_matheus)
for name in contatos2:
    contatos[name] = contatos2[name]
print(contatos)
print()
contatos.update(contatos2)
print(contatos)
print()