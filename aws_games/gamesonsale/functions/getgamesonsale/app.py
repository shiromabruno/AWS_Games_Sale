# ao inves de importar o requests inteiro, so immporta a funcao GET
# import requests
# tem um arquivo requirements.txt que indica pra funcao lambda quais libs estamos usando que nao eh BUILT IN, no caso eh o request
# coisa do python
from requests import get

import json

# pra testar a chamada, deletar o # nas linhas DELETAR

def convert_fields_to_float(game):
    #valor vinha com '123.12', vira com 123.12
    game['savings'] = float(game.get('savings'))
    game['salePrice'] = float(game.get('salePrice'))
    game['normalPrice'] = float(game.get('normalPrice'))
    return game

# context = info da execucao do lambda. Quanto de memoria, tempo de execucao...
# event = evento que estara chegando no lambda. Como eh a primeira funcao a ser invocada na maquina de estado, nao esta chegando nada
def lambda_handler(event, context):
    # volta 10 itens de jogo
    params = {'pageSize': 10}
    # retorna a quantidade de jogos = https://apidocs.cheapshark.com/
    # game_api_response --> eh uma collection que precisa transformar em dictionary, o JSON
    # a linha debaixo eh assumindo somente import requests
    # game_api_response = requests.get("https://www.cheapshark.com/api/1.0/deals", params=params)
    game_api_response = get("https://www.cheapshark.com/api/1.0/deals", params=params)
    # a resposta dos X jogos esta nesse CONTENT
    listagames = json.loads(game_api_response.content)

    #mapeamento dessa nova estrutura e transforma em lista
    return list(map(convert_fields_to_float, listagames))
 #   return listagames

 # print(json.dumps(lambda_handler({},{})))

# todos os campos como 'blabla'
# internalName = NARUTOTOBORUTOSHINOBISTRIKERDELUXEEDITION
# title = Naruto to Boruto Shinobi Striker - Deluxe Edition
# metacriticLink = None
# dealID = odTPTLrCXTor0uLaQHifLznuFqj5aPc8TC3Gm%2BLyVvw%3D
# storeID = 23
# gameID = 189692
# salePrice = 11.90
# normalPrice = 79.98
# isOnSale = 1
# savings = 85.121280
# metacriticScore = 0
# steamRatingText = none
# steamRatingPercent = 0
# steamRatingCount = 0
# steamAppID = none
# releaseDate = none
# lastChange = 1611793244
# dealRating = 10.0
# thumb = link de uma images

# test para ver a resposta printada dentro dessa funcao
#    [print(cadagame) for cadagame in listagames]

#deletarif __name__ == "__main__":
    # passando nada em event e context, codigo abaixo eh se o print tiver na funcao
    # lambda_handler({}, {})
    # codigo abaixo faz o print
#deletar print (lambda_handler({}, {}))