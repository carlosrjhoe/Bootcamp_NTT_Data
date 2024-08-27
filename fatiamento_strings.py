def main(name: str) -> None:
    print(f'Primeira letra: {name[0]}')
    print(f'Da primeira letra até nona letra: {name[:9]}')
    print(f'Apartir da 10 letra: {name[10:]}')
    print(f'Ente a 10 letra e 16 letra: {name[10:16]}')
    print(f'Nome completo: {name[:]}')
    print(f'Nome completo ao contrário: {name[::-1]}')
    

if __name__ == '__main__':
    name = 'Carlos Roberto Conceição Junior'
    main(name)