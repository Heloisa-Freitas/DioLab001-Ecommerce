
import streamlit as st
from azure.storage.blob import BlobServiceClient
import pymssql
import os
import uuid
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()
blobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
blobContainerName = os.getenv('BLOB_CONTAINER_NAME')
blobaccountName = os.getenv('BLOB_ACCOUNT_NAME')
SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

# Upload de imagem no Azure Blob
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + "_" + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f"https://{blobaccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return image_url

# Inserir produto no banco
def insert_product(product_name, product_price, product_description, product_image):
    try:
        image_url = upload_blob(product_image)
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (%s, %s, %s, %s)",
            (product_name, product_price, product_description, image_url)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f'Erro ao inserir produto: {e}')
        return False

# Buscar produtos do banco
def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT nome, preco, descricao, imagem_url FROM Produtos")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f'Erro ao listar produtos: {e}')
        return []

# Exibir produtos em cards
def list_products_screen():
    products = list_products()
    if products:
        cards_por_linha = 3
        cols = st.columns(cards_por_linha)
        for i, product in enumerate(products):
            col = cols[i % cards_por_linha]
            with col:
                st.markdown(f"### {product['nome']}")
                st.write(f"**Preço:** R$ {product['preco']:.2f}")
                st.write(f"**Descrição:** {product['descricao']}")
                if product['imagem_url']:
                    html_img = f"<img src='{product['imagem_url']}' width='200' height='200' alt='Imagem do produto'>"
                    st.markdown(html_img, unsafe_allow_html=True)
                st.markdown("---")
            if (i + 1) % cards_por_linha == 0 and (i + 1) < len(products):
                cols = st.columns(cards_por_linha)
    else:
        st.info("Nenhum produto encontrado.")

# UI principal
st.title('Cadastro de Produtos')

# Formulário
product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format="%.2f")
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'png', 'jpeg'])

if st.button('Salvar Produto'):
    if insert_product(product_name, product_price, product_description, product_image):
        st.success("Produto salvo com sucesso")
        list_products_screen()

st.markdown("## Produtos Cadastrados")

if st.button('Listar Produtos'):
    list_products_screen()
