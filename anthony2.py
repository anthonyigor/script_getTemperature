from pycep_correios import get_address_from_cep, WebService, exceptions
import requests

API_KEY = 'd959c8d47aca5dc3c2f2522df72cf295'


def getTemperature(cep):
    #busca o endereço por meio do CEP via API
    try:
        endereco = get_address_from_cep(cep, webservice=WebService.APICEP)
    except exceptions.InvalidCEP:
        print('CEP inválido.')
        return
    except exceptions.CEPNotFound:
        print('CEP não encontrado.')
        return
    cidade = endereco['cidade']

    #faz a requisição de dados do clima via API
    link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}'
    requisicao = requests.get(link_api)
    dados_requisicao = requisicao.json()

    #extrai a temperatura e converte para celsius
    temperatura = dados_requisicao['main']['temp'] - 273.15
    print(f'A temperatura atual em {cidade} é de {temperatura:.2f}°')


cep = str(input('Informe seu CEP para visualização da temperatura atual: '))
getTemperature(cep)
