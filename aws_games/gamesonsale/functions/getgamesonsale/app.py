# precisa desse import para chamar a api
import requests
import json

# context = info da execucao do lambda. Quanto de memoria, tempo de execucao...
# event = evento que estara chegando no lambda. Como eh a primeira funcao a ser invocada na maquina de estado, nao esta chegando nada
def lambda_handler(event, context):
    # volta 10 itens de jogo
    params = {'pageSize': 10}
    # retorna a quantidade de jogos = https://apidocs.cheapshark.com/
    # game_api_response --> precisa transformar em dictionary, o JSON
    game_api_response = requests.get("https://www.cheapshark.com/api/1.0/deals", params=params)
    # a resposta dos X jogos esta nesse CONTENT
    listagames = json.loads(game_api_response.content)
    return listagames

# test para ver a resposta
#    [print(cadagame) for cadagame in listagames]

if __name__ == "__main__":
    # passando nada em event e context
    lambda_handler({}, {})
