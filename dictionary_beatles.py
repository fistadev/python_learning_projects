# Criando um dicionario basico em Python
keys = ['John', 'Paul', 'George', 'Ringo']
values = ['guitar', 'bass', 'solo guitar', 'drums']

data = dict(zip(keys, values))

print(data)
# print(data['Paul'])
# print(data['Martin']) # error (not available)

# # adding values
# data['Martin'] = 'production'
# print(data)

# # remove values
# del data['John']
# print(data)
