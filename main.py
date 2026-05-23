import requests
import os
from dotenv import load_dotenv
load_dotenv()
chave = os.getenv('VT_API_KEY')
print(chave)
import re
padrao_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
lista_total_ips = []
with open('dummy_log.txt', 'r') as test:
  for linha in test:
    ips_encontrados = re.findall(padrao_ip, linha)
    lista_total_ips.extend(ips_encontrados)

lista_final_unica = list(set(lista_total_ips))

print(lista_final_unica)

for ip in lista_final_unica:
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    
    cabecalho = {
        "x-apikey": chave
    }
    
    resposta = requests.get(url, headers=cabecalho)
    
    dados = resposta.json()
    
    status = dados['data']['attributes']['last_analysis_stats']
    maliciosos = status['malicious']
    suspeitos = status['suspicious']
    
    if maliciosos > 0 or suspeitos > 0:
        print(f"🚨 IP {ip} é SUSPEITO! Detectado por {maliciosos} motores.")
    else:
        print(f"✅ IP {ip} está limpo.")