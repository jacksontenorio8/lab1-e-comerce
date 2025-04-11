# lab1-e-comerce

## Visão Geral
Este projeto é uma aplicação de e-commerce desenvolvida com **Python** e **Streamlit**, utilizando **Azure SQL** para armazenar os dados e **Azure Storage** para gerenciar as imagens dos produtos.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para desenvolvimento da aplicação.
- **Streamlit**: Framework para criação da interface do usuário.
- **Azure SQL**: Banco de dados para armazenamento de produtos e usuários.
- **Azure Storage**: Armazenamento de imagens dos produtos.

## Funcionalidades
- Cadastro de produtos com nome, descrição, preço e imagem.
- Listagem de produtos em forma de cards.
- Persistência de dados no **Azure SQL**.
- Upload e recuperação de imagens do **Azure Storage**.

## Configuração e Instalação
### Pré-requisitos
- Python 3.8+
- Conta no Azure com acesso ao **SQL Database** e **Storage**
- Dependências do projeto:
  ```sh
  pip install streamlit azure-storage-blob pyodbc pandas
  ```

### Configuração do Banco de Dados
1. Crie um banco de dados no **Azure SQL**.
2. Configure a string de conexão no arquivo `config.py`:
   ```python
   DB_CONNECTION_STRING = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=<seu-servidor>;DATABASE=<seu-banco>;UID=<usuario>;PWD=<senha>"
   ```
3. Crie a tabela para armazenar os produtos:
   ```sql
   CREATE TABLE Produtos (
       id INT IDENTITY(1,1) PRIMARY KEY,
       nome VARCHAR(255),
       descricao TEXT,
       preco DECIMAL(10,2),
       imagem_url VARCHAR(500)
   );
   ```

### Configuração do Azure Storage
1. Crie um **Storage Account** no Azure.
2. Gere uma **SAS Token** para acesso seguro.
3. Adicione as credenciais no arquivo `config.py`:
   ```python
   AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=<seu-armazem>;AccountKey=<sua-chave>;EndpointSuffix=core.windows.net"
   AZURE_CONTAINER_NAME = "produtos"
   ```

## Executando a Aplicação
1. No terminal, execute:
   ```sh
   streamlit run app.py
   ```
2. Acesse no navegador: `http://localhost:8501`

## Estrutura do Projeto
```
📂 ecommerce-project
 ┣ 📂 assets  # Armazena imagens locais (opcional)
 ┣ 📂 database  # Scripts SQL
 ┣ 📂 modules  # Módulos de backend
 ┃ ┣ 📜 database.py  # Conexão com Azure SQL
 ┃ ┣ 📜 storage.py  # Upload/download do Azure Storage
 ┣ 📂 pages  # Arquivos de interface com Streamlit
 ┃ ┣ 📜 home.py
 ┃ ┣ 📜 cadastro.py
 ┣ 📜 app.py  # Arquivo principal da aplicação
 ┣ 📜 config.py  # Configurações de conexão
 ┣ 📜 requirements.txt  # Lista de dependências
 ┗ 📜 README.md  # Documentação do projeto
```

## Próximos Passos
- Implementar autenticação de usuários.
- Melhorar a interface visual com CSS.
- Criar um dashboard para acompanhamento de vendas.

---
### Contato
Caso tenha dúvidas ou sugestões, entre em contato!


