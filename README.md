# 🛡️ Log Security Analyzer & VirusTotal Integration

Este é um script em Python desenvolvido para automatizar a análise de logs de servidores, extraindo endereços IP e verificando a reputação de cada um em tempo real utilizando a API v3 do **VirusTotal**.

Projetado para identificar rapidamente tentativas de invasão, varreduras de portas ou acessos maliciosos ocultos em grandes volumes de dados.

## 🚀 Funcionalidades

* **Extração Automatizada:** Varre arquivos de log utilizando Expressões Regulares (`re`) para capturar IPs de forma precisa.
* **Otimização de Performance:** Filtra IPs duplicados antes de realizar as requisições, economizando chamadas de API.
* **Inteligência de Ameaças:** Integração com a API do VirusTotal para checar a reputação de cada IP com múltiplos motores de segurança.
* **Segurança Prática:** Armazenamento seguro de credenciais em variáveis de ambiente (`.env`), impedindo o vazamento acidental de chaves de API.
* **Ambiente de Testes:** Acompanha um arquivo `dummy_log.txt` simulando logs reais com IPs benignos e maliciosos conhecidos para validação imediata.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Requests** (Comunicação HTTP com a API)
* **Python-Dotenv** (Gerenciamento de variáveis de ambiente)
* **Regular Expressions (re)** (Análise de texto/padrões)

## 📦 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO