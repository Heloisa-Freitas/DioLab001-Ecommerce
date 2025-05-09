# DioLab001 - Ecommerce com Streamlit e Azure

Este projeto é uma aplicação web de cadastro de produtos desenvolvida com **Streamlit** e implantada na nuvem usando o **Azure App Service**, com infraestrutura definida desde o provisionamento da aplicação até a automação de inicialização.

##  Tecnologias Utilizadas

- Python 3.12
- Streamlit
- Azure App Service (Linux)
- Azure SQL Database
- Azure Blob Storage
- PyMSSQL
- azure-storage-blob
- dotenv

##  Infraestrutura

A infraestrutura do projeto foi baseada no provisionamento manual dos seguintes recursos no **Microsoft Azure**:

- **Azure App Service**: ambiente de execução Python 3.12 com publicação via código (manual).
- **Azure SQL Database**: base relacional para persistência dos dados dos produtos.
- **Azure Blob Storage**: armazenamento de imagens dos produtos.

##  Estrutura do Projeto

```
📦Projeto
 ┣ 📜main.py                  # Código principal da aplicação Streamlit
 ┣ 📜requirements.txt         # Dependências da aplicação
 ┣ 📜.env                     # Variáveis de ambiente sensíveis (não versionado)
 ┣ 📜.env.example             # Exemplo de estrutura de variáveis
 ┣ 📜startup.sh               # Script de inicialização usado pelo App Service
 ┣ 📜.gitignore               # Exclusões importantes
 ┗ 📜README.md                # Documentação do projeto
```

##  Funcionalidades

- Cadastro de produtos com nome, preço, descrição e imagem.
- Armazenamento das informações no Azure SQL.
- Upload das imagens no Azure Blob Storage.
- Interface 100% web usando Streamlit.
- Suporte a arquivos `.env` com conexão segura aos serviços do Azure.

##  Configuração Local

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .venv\Scripts\activate       # Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` com base no `.env.example`.

4. Execute a aplicação localmente:
   ```bash
   streamlit run main.py
   ```

##  Deploy no Azure App Service via VS Code

1. Instale a extensão **Azure App Service** no VS Code.
2. Faça login com sua conta Azure dentro do VS Code.
3. No painel lateral do Azure:
   - Clique com o botão direito sobre o App Service criado.
   - Selecione **"Deploy to Web App..."**.
   - Escolha o diretório do projeto.
4. O VS Code empacota e publica o código automaticamente.
5. A aplicação será iniciada usando o `startup.sh` configurado com:
   ```bash
   #!/bin/bash
   echo "Iniciando aplicação..."
   streamlit run main.py --server.port=8000 --server.enableCORS=false
   ```

---

##  Resultado Final

Aplicação hospedada em Azure com URL pública, conectada a banco de dados e armazenamento, com deploy automatizado via VS Code e suporte a variáveis de ambiente.

##  Screenshots


Template em Codigo json para criacao de database e do blob storage
![image](https://github.com/user-attachments/assets/e065e60e-dc63-43fd-ae15-0c4b909e5ee2)

![image](https://github.com/user-attachments/assets/08c475c1-8cc1-4dd6-b8c3-7b60fd9d1300)

![image](https://github.com/user-attachments/assets/e37fc217-d901-4f08-9f6a-ee1d3373d2f1)

Criacao da Tabela Produtos no Query Editor
![image](https://github.com/user-attachments/assets/2dff623b-0201-47e4-9e83-2e297d5aa4cc)

Codigo e estrutura
![image](https://github.com/user-attachments/assets/8ceebc28-336c-4538-96d6-d82377f18879)

App Service
![image](https://github.com/user-attachments/assets/065e3285-65a7-416c-a53b-621e190783b9)

Deploy no App Service
![Screenshot 2025-05-09 104801](https://github.com/user-attachments/assets/422f1a11-4fdb-4cef-ac7b-027a6920df02)









