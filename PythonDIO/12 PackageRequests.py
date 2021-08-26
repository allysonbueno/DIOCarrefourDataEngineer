# Instalando e utilizando pacotes em Python e realizar requisição com requests
# configurei pip nas variaveis de ambiente
# rodei o pip install requests

import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    # print(response.text)
    print(response.json())
    # print(type(response.text))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return(dados_cep)
def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # retorna_dados_cep('87023100')

    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)
    # print(dados_pokemon['sprites'],['front_shiny'])

    response = retorna_response('https://web.digitalinnovation.one/')
    print(response)

    # raspagem de dados