#!/bin/bash
echo "Iniciando aplicação..."
python3 -m streamlit run main.py --server.port=8000 --server.enableCORS=false
