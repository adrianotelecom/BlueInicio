perguntas = [("Nome","Gustavo"),("Idade","30")]
respostas = [("Sexo","Masculino"),("Altura","1.70")]
perguntas_dict = dict (perguntas)
respostas_dict = dict (respostas)
for k,v in perguntas_dict.items():
    print(f'{k} - {v} ')
for k,v in respostas_dict.items():
    print(f'{k} - {v} ')