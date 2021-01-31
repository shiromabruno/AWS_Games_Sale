# ao inves de importar o requests inteiro, so immporta a funcao GET
# import requests
from requests import get
import json

# pra testar a chamada, deletar o # nas linhas DELETAR

# DELETAR from functions.getgamesonsale.app import lambda_handler as getgameonsale

# context = info da execucao do lambda. Quanto de memoria, tempo de execucao...
# event = evento que estara chegando no lambda. Como eh a primeira funcao a ser invocada na maquina de estado, nao esta chegando nada
def lambda_handler(event, context):
    params = {'base': 'USD'}
    # a linha debaixo eh assumindo import requests
    # currency_api_response = requests.get("https://api.exchangeratesapi.io/latest", params=params)
    currency_api_response = get("https://api.exchangeratesapi.io/latest", params=params)
    current_currency = json.loads(currency_api_response.content)

# tratar o event que eh o jogo que estara recebendo, e vou pegar o normalPrice do evento, multiplicar pelo valor da moeda BRL do USD
# o valor eh grande do FLOAT, entao formata a saida pra ter apenas 2 casas decimais dps da virgula
    event['normalPrice'] = "{:.2f}".format(event.get('normalPrice') * current_currency.get('rates').get('BRL'))
    event['salePrice'] = "{:.2f}".format(event.get('salePrice') * current_currency.get('rates').get('BRL'))

    return event

    # 'rates': {'CAD': 1.2788398154, 'HKD': 7.7532135794,...'PLN': 3.7330257086}, 'base': 'USD', 'date': '2021-01-29'}
#    return current_currency  --> traz tudo acima. O de baixo so traz o BRL
#    return current_currency.get('rates').get('BRL')
   # retorno trazido do comando acima : 5.4851680949



# DELETAR if __name__ == "__main__":
    # passando nada em event e context, codigo abaixo eh se o print tiver na funcao
    # lambda_handler({}, {})
    # codigo abaixo faz o print
# DELETAR     games = getgameonsale({}, {})
# DELETAR    print (lambda_handler(games[0], {}))