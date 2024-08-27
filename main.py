# texto = input('Digite seu nome: ')
# VOGAIS = 'AEIOU'
# lista = []
#
# for letra in texto:
#     if letra.upper() in VOGAIS:
#         # print(f'{letra}', end=' ')
#         lista.append(letra.upper())
#
# print(f'{lista}')
# # print(list(range(4)))

def main(string: int):
    while string != 3:
        string = int(input('[1] Sacar \n[2] Extrato \n[3] Sair\n:'))
        if string == 1:
            print('Sacando...')
        elif string == 2:
            print('Exibindo o extrato...')
        else:
            print('Saindo...')

if __name__ == '__main__':
    opcao: int = 0
    main(opcao)
