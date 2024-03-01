from flask import Blueprint, render_template, request, redirect, url_for
from models import Produto
from app import db

cadastrar_routes = Blueprint('cadastrar_routes', __name__)

@cadastrar_routes.route("/produto/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@cadastrar_routes.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")
    
    if nome and descricao and valor:
        p = Produto(nome, descricao, valor)

        db.session.add(p)
        db.session.commit()
    
    return redirect(url_for("index"))
