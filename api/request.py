import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_data_from_api():
	try:
		url = os.getenv("API_URL")

		querystring = os.getenv("API_QUERYSTRING")

		headers = {
			"x-rapidapi-key":  os.getenv("API_HEADERS_KEY"),
			"x-rapidapi-host": os.getenv("API_HEADERS_HOST")
		}

		response = requests.get(url, headers=headers, params=querystring)

		data_dict = response.json()
			
		# Acessar o valor da chave 'data'
		data = data_dict.get('data')
		print("A requisição foi concluida com sucesso")
		return data
	except Exception as e:
    		print('Erro durante a requisição', e)
