import os
import requests

url = "https://dados.antt.gov.br/dataset/7c6bc8ab-69fb-4955-9cf3-7481cfa089f9/resource/f8ead9f7-b4d2-40a1-94b5-96e1b852e243/download/investimentos_autorizados_gpfer_pip.json"

if(os.path.exists("investimentos.json")):
    print("Arquivo já existe!")
else:
    response = requests.get(url)

if response.status_code == 200:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "investimentos.json")
    
    with open(file_path, "w") as file:
        file.write(response.text)
        print("Arquivo salvo com sucesso!")
else:
    print("Erro ao fazer a requisição:", response.status_code)