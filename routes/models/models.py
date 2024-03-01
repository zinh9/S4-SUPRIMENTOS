from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import DECIMAL
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

class Produto(db.Model):
    __tablename__ = 'produto'

    idProduto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    valor = db.Column(DECIMAL(precision=10, scale=2))

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor