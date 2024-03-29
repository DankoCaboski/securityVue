import json
import os
import requests

print("Diretório de trabalho atual:", os.getcwd())
print("O arquivo 'investimentos.json' existe:", os.path.exists('investimentos.json'))

url = "https://dados.antt.gov.br/dataset/7c6bc8ab-69fb-4955-9cf3-7481cfa089f9/resource/f8ead9f7-b4d2-40a1-94b5-96e1b852e243/download/investimentos_autorizados_gpfer_pip.json"

response = requests.get(url)
data = response.json()

with open('inserts.sql', 'w') as file:
    for record in data:
       print(record)
       insert_statement = f"INSERT INTO investimentos (titulo, numero_processo, ato_portaria_deliberacao, data_da_publicacao, concessionaria, estado) VALUES ('{record['0']}', '{record['1']}', '{record['2']}', '{record['3']}', '{record['4']}', '{record['5']}');\n"
        
       file.write(insert_statement)