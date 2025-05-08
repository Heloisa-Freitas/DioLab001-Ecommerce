#!/bin/bash

echo "Iniciando startup.sh..."

# Ativa o ambiente virtual criado automaticamente pelo Oryx
source /home/site/wwwroot/antenv/bin/activate

# Executa o app Streamlit
python3 -m streamlit run main.py --server.port=8000 --server.enableCORS=false
