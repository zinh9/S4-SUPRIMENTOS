# Arquivo para atualizar as informações de um produto. UPDATE da função CRUD

from flask import Blueprint, render_template, request, redirect, url_for # Importa o Blueprint e outras classes e funções necessárias do Flask
from models import db, Produto # Importa o objeto do banco de dados e os modelos de produto definidos em models.py

# Blueprint para as rotas de atualização de produtos
atualizar_routes = Blueprint('atualizar_routes', __name__)

# Rota para atualizar um produto pelo seu ID
@atualizar_routes.route("/atualizar/<int:idProduto>", methods=['POST', 'GET'])
def atualizar(idProduto):
    # Consulta o produto pelo ID
    produto = Produto.query.filter_by(idProduto = idProduto).first()

    # Verifica o método HTTP da requisição
    if request.method == 'POST':
         # Obtém os dados do formulário
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")

        # Verifica se todos os campos foram preenchidos
        if nome and descricao and valor:
            # Atualiza os atributos do produto
            produto.nome = nome
            produto.descricao = descricao
            produto.valor = valor

            # Salva as mudanças no banco de dados
            db.session.commit()

            # Redireciona para a página inicial
            return redirect(url_for("index"))
    
    # Renderiza o template de atualização com os dados do produto
    return render_template("atualizar_produto.html", produto=produto)
