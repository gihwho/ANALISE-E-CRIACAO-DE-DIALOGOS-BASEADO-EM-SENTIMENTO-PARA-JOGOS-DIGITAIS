import requests

url = "http://127.0.0.1:5000/generate"
data = {"prompt": "A unit died being shot by a cannonball"}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    print("Resposta da API:", response.json())
else:
    print("Erro na requisição:", response.status_code)
    print("Detalhes:", response.text)
