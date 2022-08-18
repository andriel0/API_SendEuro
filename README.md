# API_send_euro

As vezes trabalho como freelancer de um site internacional que paga em Euro e eu senti uma necessidade de saber a cotação do Euro todo dia para saber o melhor dia para eu converter.
Então automatizei o processo com 2 API's, uma de cotação de moedas e uma de envio de SMS.
- Eu recebi a cotação do Euro em JSON, converti para dicionários Python.
- Peguei o valor do Euro atualizado e coloquei no corpo da mensagem do SMS.
- Enviei o SMS para meu celular.
- Coloquei a API em um servidor, Heroku, e recebo um SMS com a cotação atualizada do Euro toda manhã como programei no servidor.
