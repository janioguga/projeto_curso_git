import requests
def busca_cep ():
    response = requests.get ('https://viacep.com.br/ws/59086200/json/')
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep ['logradouro'])
    print(dados_cep[ 'complemento'])

def retorna_response(url):
    response = requests.get(url)
    response.headers
    return response.text



busca = requests.get('https://viacep.com.br/ws/01001000/json/')
status = busca.status_code

def interpretarMensagem(mensagem):
  print('{} {}'.format())

if status == 400:
  print('Mensagem não chegou')
elif status == 200:
  mensagem = busca.json()
  interpretarMensagem(mensagem)
#fim do código.


#if __name__ == '__main__':
    #response = retorna_response('https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/')


