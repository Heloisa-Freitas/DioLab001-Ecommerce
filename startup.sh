#!/bin/bash
echo "Iniciando aplicação..."
source antenv/bin/activate
python -m streamlit run main.py --server.port=8000 --server.enableCORS=false
