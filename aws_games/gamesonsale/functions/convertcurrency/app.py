# tem um arquivo requirements.txt que indica pra funcao lambda quais libs estamos usando que nao eh BUILT IN, no caso eh o request
# coisa do python
from requests import get
import json
from uuid import uuid4


def create_payload(game, moedabrl):
    return{
        'id': str(uuid4()),
        'title': game.get("title"),
        'normalPrice': "{:.2f}".format(game.get('normalPrice') * moedabrl),
        'salePrice':  "{:.2f}".format(game.get('salePrice') * moedabrl)
    }

def lamda_handler(event, context):
    params = {'base': 'USD'}
    currency_api_response = get("https://api.exchangeratesapi.io/latest", params=params)
    # o event debaixo sera o proprio game recebido
    return create_payload(event, json.loads(currency_api_response.content).get('rates').get('BRL'))

