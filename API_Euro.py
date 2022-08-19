from twilio.rest import Client
import requests
import time

str_hora = "%d/%m/%y %H:%M:%S"
hora = time.strftime(str_hora)

def mostrar_euro(link):
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    cotacao_euro = float(requisicao_dic["EURBRL"]["bid"])
    msg = 'Cotação Atualizada. {} \nEuro: R$ {}'.format(hora, cotacao_euro)
    return msg

euro = mostrar_euro("https://economia.awesomeapi.com.br/last/EUR-BRL")

account_sid = 'XXXX'
token = 'YYYYY'

client = Client(account_sid, token)

numero_envio = '+12517328233'
numero_recebe = '+5585996953190'

message = client.messages.create(
          to=numero_recebe,
          from_=numero_envio,
          body=euro)
print(message.sid)
