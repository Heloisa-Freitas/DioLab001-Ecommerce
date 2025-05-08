#!/bin/bash

# Ativar o ambiente virtual (se criado com o GitHub Actions, pode estar em /antenv ou similar)
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d "antenv" ]; then
    source antenv/bin/activate
fi

# Executar o app Streamlit
streamlit run main.py --server.port=8000 --server.enableCORS=false
