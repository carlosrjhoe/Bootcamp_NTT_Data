import requests

def obter_pessoas():
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados['results']
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return None

def exibir_pessoas(pessoas):
    if pessoas:
        for pessoa in pessoas:
            print(f"Nome: {pessoa['name']}")
            print(f"Altura: {pessoa['height']} cm")
            print(f"Peso: {pessoa['mass']} kg")
            print(f"Cor do cabelo: {pessoa['hair_color']}")
            print(f"Cor da pele: {pessoa['skin_color']}")
            print(f"Cor dos olhos: {pessoa['eye_color']}")
            print(f"Ano de nascimento: {pessoa['birth_year']}")
            print(f"Gênero: {pessoa['gender']}")
            print("-" * 40)
    else:
        print("Nenhuma pessoa foi encontrada.")

def main():
    pessoas = obter_pessoas()
    exibir_pessoas(pessoas)

if __name__ == "__main__":
    main()
