from flask import Blueprint, render_template, redirect, url_for
from models import db, Produto

excluir_routes = Blueprint('excluir_routes', __name__)

@excluir_routes.route("/excluir/<int:idProduto>")
def excluir(idProduto):
    produto = Produto.query.filter_by(idProduto = idProduto).first()

    if produto:
        db.session.delete(produto)
        db.session.commit()

    produtos = Produto.query.all()

    return render_template("lista.html", produtos = produtos)
