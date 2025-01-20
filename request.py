import requests
import json

url = "https://youtube-data16.p.rapidapi.com/popularVideos"

querystring = {"videoCategoryId":"2","regionCode":"BR","maxResults":"50","hl":"en"}

headers = {
	"x-rapidapi-key": "07d3d2d00amsh075e91bf1a72ae4p17ed33jsn80c05c256f15",
	"x-rapidapi-host": "youtube-data16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data_dict = response.json()
    
# Acessar o valor da chave 'data'
data = data_dict.get('data')
    
# Exibir o conteúdo de 'data'
print(data)
