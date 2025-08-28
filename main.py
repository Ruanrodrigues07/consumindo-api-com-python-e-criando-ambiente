from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')

def hello_word():
    '''
    Endpoint que exibe uma mensagem incrivel do mundo da programação
    '''
    return {'Hello': 'Word'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint que retorna o cardápio de um restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurantes = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurantes.append({
                    'item': item['Item'],
                    'price': item['price'], 
                    'description': item['description']
            })
        return {'Restaurante':restaurante, 'Cardápio': dados_restaurantes}

    else:
        return {f'Erro: {response.status_code} - {response.text}'}