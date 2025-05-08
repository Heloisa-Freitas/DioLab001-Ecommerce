#!/bin/bash
echo "Iniciando startup.sh..."

# Ativa o ambiente virtual criado no build
source antenv/bin/activate

# Executa o app Streamlit
streamlit run main.py --server.port=8000 --server.enableCORS=false
