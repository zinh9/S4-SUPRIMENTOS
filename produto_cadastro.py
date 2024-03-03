# Arquivo para adicionar um produto. CREATE da função CRUD

from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Produto

# Blueprint para as rotas de cadastro de produtos
cadastrar_routes = Blueprint('cadastrar_routes', __name__)

# Rota para renderizar a página de cadastro de produto
@cadastrar_routes.route("/produto/cadastrar")
def cadastrar_produto():
    return render_template("adicionar_produto.html")

# Rota para cadastrar um novo produto
@cadastrar_routes.route("/cadastro", methods=['POST', 'GET'])
def cadastro_produto():
    if request.method == 'POST':
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")
    
    if nome and descricao and valor:
        # Cria um novo objeto Produto com os dados fornecidos
        p = Produto(nome, descricao, valor)

        # Adiciona o novo produto ao banco de dados
        db.session.add(p)
        db.session.commit()
    
    # Redireciona para a rota da página principal
    return redirect(url_for("index"))
