lista = ['uva', 'laranja', 'maçã', 'banana', 'pera']
# lista = ['P', 'y', 't', 'h', 'o', 'n']
# numeros = [1, 2, 3, 4, 5 , 10, 12, 13, 14, 16, 17, 18]
# pares = []
# impar = []


# print(f'{lista}')
# print(lista[0])
# print(lista[-1])
# print(lista[1:3])
# print(lista[::-1])

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impar.append(numero)

# pares = [numero for numero in numeros if numero % 2 == 0]
# impar = [numero for numero in numeros if numero % 2 != 0]
# quadrado = [numero ** 2 for numero in numeros]

nuemros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

# lista.sort(key=lambda fruta: len(fruta))
# print(lista)

print(nuemros)