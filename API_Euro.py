from twilio.rest import Client
import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")

requisicao_dic = requisicao.json()
cotacao_euro = requisicao_dic["EURBRL"]["bid"]

#Tirando o account_sid e o token para preservar a conta
account_sid = 'XXXX'
token = 'YYYYY'

client = Client(account_sid, token)

numero_envio = '+12517328233'
numero_recebe = '+5585996953190'
msg = 'Cotação Atualizada. {}\nEuro: R$ {}'.format(datetime.now(), cotacao_euro)
msg = str(msg)

message = client.messages.create(
    to = numero_recebe,
    from_ = numero_envio,
    body = msg)
print(message.sid)
