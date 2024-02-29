from flask import Blueprint, render_template, request, redirect, url_for
from models import Produto, db

atualizar_routes = Blueprint('atualizar_routes', __name__)

@atualizar_routes.route("/atualizar/<int:idProduto>", methods=['POST', 'GET'])
def atualizar(idProduto):
    produto = Produto.query.filter_by(idProduto = idProduto).first()

    if request.method == 'POST':
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")
    
        if nome and descricao and valor:
            produto.nome = nome
            produto.descricao = descricao
            produto.valor = valor

            db.session.commit()

            return redirect(url_for("listar_routes.lista"))
    
    return render_template("atualizar.html", produto=produto)
