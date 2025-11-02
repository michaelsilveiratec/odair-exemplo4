# 🔗 SHEIN API - FastAPI Backend

<div align="center">

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-100000?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-00AA40?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

![Status](https://img.shields.io/badge/Status-Live_%F0%9F%9A%80-success?style=for-the-badge)
![Docs](https://img.shields.io/badge/Docs-Swagger_%F0%9F%93%96-blue?style=for-the-badge)
![CRUD](https://img.shields.io/badge/CRUD-Complete_%E2%9C%85-green?style=for-the-badge)

**RESTful API for SHEIN Sales Data**  
_Powered by FastAPI & PostgreSQL_

</div>

---

## 🎯 Visão Geral
A **SHEIN API** é uma API RESTful construída com **FastAPI** que fornece endpoints completos para **gerenciamento e análise de dados de produtos e vendas** da SHEIN.  
Inclui operações **CRUD**, **análises agregadas** e **documentação interativa automática** com Swagger e Redoc.

---

## ✨ Funcionalidades Principais
- 🏗️ **CRUD Completo** para produtos  
- 📊 **Análises Agregadas** por categoria e marca  
- 📚 **Documentação Interativa** com Swagger e Redoc  
- 🐳 **Containerização** com Docker  
- 🗄️ **ORM SQLAlchemy** com PostgreSQL  
- ✅ **Validação de Dados** com Pydantic  

---

## 🚀 Início Rápido

### 🧩 Pré-requisitos
```bash

▶️ Via Docker (Recomendado)
# Na raiz do projeto
docker-compose up --build api

# Ou apenas a API com o banco
docker-compose up db api

💻 Via Python Local
# Navegue até a pasta da API
cd api

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
uvicorn main:app --reload --host 0.0.0.0 --port 8000

🌐 Acesso
🔗 API:  http://localhost:8000
📚 Docs: http://localhost:8000/docs

🏗️ Estrutura do Projeto
api/
├── 🐳 Dockerfile                 # Containerização
├── 🐍 main.py                   # Aplicação principal FastAPI
├── 📋 requirements.txt          # Dependências Python
└── 📁 models/                   # Modelos de dados (opcional)
    ├── 🗄️ database.py          # Configuração do banco
    └── 🏷️ schemas.py           # Schemas Pydantic

📡 Endpoints da API
🏠 Endpoints Básicos
Método	Endpoint	Descrição
GET	/	Mensagem de boas-vindas
GET	/health	Status da API
📦 Endpoints de Produtos (CRUD)
Método	Endpoint	Descrição
GET	/produtos/	Lista todos os produtos
GET	/produtos/{id}	Obtém um produto por ID
POST	/produtos/	Cria um novo produto
PUT	/produtos/{id}	Atualiza um produto existente
DELETE	/produtos/{id}	Remove um produto
📊 Endpoints de Análise
Método	Endpoint	Descrição
GET	/categorias/	Vendas totais por categoria
GET	/marcas/	Vendas totais por marca
🎮 Como Usar
📋 Listar Produtos
curl -X 'GET' 'http://localhost:8000/produtos/' -H 'accept: application/json'

🔍 Obter Produto por ID
curl -X 'GET' 'http://localhost:8000/produtos/1' -H 'accept: application/json'

➕ Criar Produto
curl -X 'POST' 'http://localhost:8000/produtos/' \
  -H 'Content-Type: application/json' \
  -d '{
    "nome": "Novo Produto",
    "categoria": "Roupas",
    "marca": "SHEIN",
    "preco": 99.90,
    "estoque": 100,
    "vendas": 0
  }'

✏️ Atualizar Produto
curl -X 'PUT' 'http://localhost:8000/produtos/1' \
  -H 'Content-Type: application/json' \
  -d '{
    "preco": 129.90,
    "estoque": 150
  }'

🗑️ Deletar Produto
curl -X 'DELETE' 'http://localhost:8000/produtos/1'

📈 Análise por Categoria
curl -X 'GET' 'http://localhost:8000/categorias/' -H 'accept: application/json'

🗄️ Modelo de Dados
🧩 Tabela: produtos
Coluna	Tipo	Descrição
id	Integer	Chave primária
nome	String(100)	Nome do produto
categoria	String(50)	Categoria do produto
marca	String(100)	Marca do produto
preco	Float	Preço do produto
estoque	Integer	Quantidade em estoque
vendas	BigInteger	Total de vendas
🧱 Schema Pydantic
class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    marca: str
    preco: float
    estoque: int
    vendas: int

🔧 Configuração
⚙️ Variáveis de Ambiente
# No código main.py
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/sheindb")

🗃️ Conexão com Banco de Dados
postgresql://postgres:postgres@db:5432/sheindb

🧩 Configuração do Docker
# docker-compose.yml
api:
  build: ./api
  environment:
    DATABASE_URL: postgresql://postgres:postgres@db:5432/sheindb
  ports:
    - "8000:8000"

🛠️ Desenvolvimento
💻 Instalação para Desenvolvimento
cd api
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

pip install -r requirements.txt
uvicorn main:app --reload

📁 Estrutura do Código
# main.py - Estrutura principal
├── Importações e configuração
├── Modelo SQLAlchemy (Produto)
├── Schemas Pydantic
├── Configuração do banco
├── Aplicação FastAPI
├── Endpoints CRUD
└── Endpoints de análise

🧩 Dependências Principais
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pydantic==2.5.0

🐳 Docker
🧱 Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

⚙️ Comandos Docker Úteis
# Build da imagem
docker build -t shein-api .

# Executar container
docker run -p 8000:8000 shein-api

# Ver logs
docker logs <container_id>

# Parar container
docker stop <container_id>

🔍 Solução de Problemas
❌ API não conecta ao banco
docker-compose ps db
docker-compose logs api

❌ Erro de importação
pip install -r requirements.txt
docker-compose build api

❌ Endpoints retornam erro 500
docker-compose logs api
curl http://localhost:8000/health

📊 Exemplos de Resposta
✅ Health Check
{
  "status": "healthy",
  "message": "API está funcionando"
}

✅ Lista de Produtos
[
  {
    "id": 1,
    "nome": "Calça Jeans Feminina Skinny",
    "categoria": "Calça",
    "marca": "SHEIN BASICS",
    "preco": 129.9,
    "estoque": 120,
    "vendas": 10500
  }
]

✅ Análise por Categoria
{
  "Calça": 19209,
  "Camisa": 18200,
  "Eletrônicos": 16500,
  "Roupas": 29500
}

🎨 Documentação Interativa

📚 Swagger UI: http://localhost:8000/docs

📄 Redoc: http://localhost:8000/redoc

<div align="center">

🚀 Pronto para Usar!
Acesse: http://localhost:8000/docs

Desenvolvido com 💙 por Jadson Porto & Michael Ramos
Impacta Tecnologia - 2025

⭐ Contribuições são bem-vindas!

</div> ```
# Docker e Docker Compose instalados
# Ou Python 3.8+ para execução local
