import streamlit as st
import pyodbc
from azure.storage.blob import BlobServiceClient
import os

# Configurações
DB_CONNECTION_STRING = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=<seu-servidor>;DATABASE=<seu-banco>;UID=<usuario>;PWD=<senha>"
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=<seu-armazem>;AccountKey=<sua-chave>;EndpointSuffix=core.windows.net"
AZURE_CONTAINER_NAME = "produtos"

# Função para conectar ao banco de dados
def get_db_connection():
    return pyodbc.connect(DB_CONNECTION_STRING)

# Função para inserir produto no banco de dados
def insert_product(nome, descricao, preco, imagem_url):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Produtos (nome, descricao, preco, imagem_url)
        VALUES (?, ?, ?, ?)
    """, (nome, descricao, preco, imagem_url))
    conn.commit()
    conn.close()

# Função para buscar produtos
def fetch_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, descricao, preco, imagem_url FROM Produtos")
    products = cursor.fetchall()
    conn.close()
    return products

# Função para fazer upload de imagem no Azure Storage
def upload_image_to_azure(image_file):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=image_file.name)
    blob_client.upload_blob(image_file, overwrite=True)
    return f"https://{blob_service_client.account_name}.blob.core.windows.net/{AZURE_CONTAINER_NAME}/{image_file.name}"

# Interface com Streamlit
st.title("E-Commerce com Streamlit e Azure")

# Formulário de cadastro de produtos
with st.form("product_form"):
    nome = st.text_input("Nome do Produto")
    descricao = st.text_area("Descrição")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    imagem = st.file_uploader("Imagem do Produto", type=["png", "jpg", "jpeg"])
    submit_button = st.form_submit_button("Cadastrar")
    
    if submit_button:
        if nome and descricao and preco and imagem:
            imagem_url = upload_image_to_azure(imagem)
            insert_product(nome, descricao, preco, imagem_url)
            st.success("Produto cadastrado com sucesso!")
        else:
            st.error("Todos os campos são obrigatórios!")

# Exibir produtos cadastrados
st.header("Produtos Cadastrados")
products = fetch_products()
if products:
    for product in products:
        st.image(product[4], width=200)
        st.subheader(product[1])
        st.write(product[2])
        st.write(f"**Preço:** R$ {product[3]:.2f}")
        st.markdown("---")
else:
    st.write("Nenhum produto cadastrado ainda.")
