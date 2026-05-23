# 🛡️ Log Security Analyzer 

Este é um script em Python desenvolvido para automatizar a análise de logs de servidores, extraindo endereços IP e verificando a reputação de cada um em tempo real utilizando a API v3 do **VirusTotal**.

Criei esse projeto para praticar:
- leitura de arquivos
- regex
- consumo de API
- automação de análise de logs
- uso de variáveis de ambiente com `.env`

## Funcionalidades

- Extrai IPs automaticamente de logs
- Remove IPs duplicados
- Consulta reputação no VirusTotal
- Usa `.env` para proteger a chave da API
- Inclui um arquivo `dummy_log.txt` para testes

## Tecnologias Utilizadas

* **Python 3**
* **Requests** (Comunicação HTTP com a API)
* **Python-Dotenv** (Gerenciamento de variáveis de ambiente)
* **Regular Expressions (re)** (Análise de texto/padrões)

## Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/matheuslach83131-coder/log-analyzer.git
   cd log-analyzer
   ```

## Configuração da API

Crie um arquivo `.env`:

```env
VT_API_KEY=sua_chave_aqui
```

## Exemplo de saída

IP: 185.xxx.xxx.xxx
Detecções maliciosas: 12
Status: SUSPEITO

IP: 8.8.8.8
Detecções maliciosas: 0
Status: LIMPO
