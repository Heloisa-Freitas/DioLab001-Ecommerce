#!/bin/bash
echo "Iniciando aplicação..."

# Ativa o ambiente virtual criado automaticamente pelo Azure
source antenv/bin/activate

# Executa o Streamlit
python3 -m streamlit run main.py --server.port=8000 --server.enableCORS=false