from flask_sqlalchemy import SQLAlchemy # Importa a classe SQLAlchemy do Flask SQLAlchemy
from sqlalchemy.types import DECIMAL # Importa o tipo DECIMAL do SQLAlchemy

# Instância chamada db do SQLAlchemy para interagir com o banco de dados
db = SQLAlchemy()

# Classe de modelo de dados para usuários
class Usuario(db.Model):
    __tablename__ = 'usuario' # Especifíca o nome da tabela de registros de usuários no banco de dados 

    # Atributos definidos idênticos a cada coluna na tabela Usuario
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)

    # Objeto com os parâmetros de email e senha
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

# Classe de modelo de dados para produtos
class Produto(db.Model):
    __tablename__ = 'produto' # Especifíca o nome da tabela de registros de produtos no banco de dados

    # Atributos definidos idênticos a cada coluna na tabela Produto
    idProduto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    valor = db.Column(DECIMAL(precision=10, scale=2))

    # Objeto com os parâmetros de nome do produto, descrição do produto e valor do produto
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor