# pessoa = {'nome': 'carlos', 'idade': 38}

# pessoa['sobrenome'] = 'junior'

# print(pessoa)
# print(pessoa['nome'])
# print(pessoa['sobrenome'])
# print(pessoa['idade'])

# pessoa['nome'] = 'mayara'
# print(pessoa)
# print(pessoa['nome'])
# print(pessoa['sobrenome'])
# print(pessoa['idade'])

contatos = {
    'carlosrjhoe@gmail.com': {'nome': 'carlos', 'sobrenome': 'junior'},
    'mayara@gmail.com': {'nome': 'mayara', 'sobrenome': 'ramos'},
    'carlosrneto@gmail.com': {'nome': 'carlos', 'sobrenome': 'neto'},
    'luna@gmail.com': {'nome': 'luna', 'sobrenome': 'ramos'}
}

# print(contatos['luna@gmail.com']['sobrenome'])
# print(contatos['carlosrneto@gmail.com']['nome'])

for c, v in contatos.items():
    print(f"Email: {c} | nome: {v['nome'].title()}, sobrenome: {v['sobrenome'].title()}")