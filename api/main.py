from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional
import os

# Configuração da conexão com o banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/sheindb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modelo da tabela produtos
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    marca = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    vendas = Column(BigInteger, nullable=False)

# Modelo Pydantic para validação (criação)
class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    marca: str
    preco: float
    estoque: int
    vendas: int

    class Config:
        from_attributes = True

# Modelo Pydantic para atualização (todos os campos opcionais)
class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None
    marca: Optional[str] = None
    preco: Optional[float] = None
    estoque: Optional[int] = None
    vendas: Optional[int] = None

    class Config:
        from_attributes = True

# Cria a tabela se não existir
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SHEIN API", description="API completa para gerenciamento de produtos SHEIN")

# Dependency para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Shein", "docs": "/docs"}

@app.get("/produtos/")
def listar_produtos():
    db = SessionLocal()
    produtos = db.query(Produto).all()
    db.close()
    return produtos

@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    db = SessionLocal()
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    db.close()
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos/")
def criar_produto(produto: ProdutoBase):
    db = SessionLocal()
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    db.close()
    return db_produto

@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto_update: ProdutoUpdate):
    db = SessionLocal()
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if produto is None:
        db.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Atualiza apenas os campos fornecidos
    update_data = produto_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(produto, field, value)
    
    db.commit()
    db.refresh(produto)
    db.close()
    return produto

@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    db = SessionLocal()
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if produto is None:
        db.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(produto)
    db.commit()
    db.close()
    return {"message": "Produto deletado com sucesso", "produto_id": produto_id}

@app.get("/categorias/")
def analise_categorias():
    db = SessionLocal()
    query = db.query(Produto.categoria, func.sum(Produto.vendas).label("total_vendas")).group_by(Produto.categoria).all()
    db.close()
    return {categoria: total_vendas for categoria, total_vendas in query}

@app.get("/marcas/")
def analise_marcas():
    db = SessionLocal()
    query = db.query(Produto.marca, func.sum(Produto.vendas).label("total_vendas")).group_by(Produto.marca).all()
    db.close()
    return {marca: total_vendas for marca, total_vendas in query}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API está funcionando"}