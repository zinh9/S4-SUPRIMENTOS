from flask import Blueprint, render_template, redirect, url_for
from models import db, Produto

# Blueprint para as rotas de exclusão de produtos
excluir_routes = Blueprint('excluir_routes', __name__)

# Rota para excluir um produto pelo ID
@excluir_routes.route("/excluir/<int:idProduto>")
def excluir(idProduto):
    # Procura o produto pelo ID no banco de dados
    produto = Produto.query.filter_by(idProduto = idProduto).first()

    if produto: # Verifica se o produto existe
        # Remove o produto do banco de dados
        db.session.delete(produto)
        db.session.commit()

    # Recupera todos os produtos após a exclusão
    produtos = Produto.query.all()

    return render_template("index.html", produtos = produtos)
