from flask import Blueprint, render_template
from routes.models import db, Produto

listar_routes = Blueprint('listar_routes', __name__)

@listar_routes.route("/produto/listar")
def lista():
    produtos = Produto.query.all()
    return render_template("lista.html", produtos=produtos)
