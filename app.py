"""
Este arquivo contém a configuração e definição das rotas principais de uma aplicação web Flask,
juntamente com a importação de modelos de banco de dados e blueprints relacionados ao cadastro
de usuários, login, e operações CRUD de produtos, incluindo o READ da função CRUD na página principal.
"""

from flask import Flask, render_template, request, url_for, redirect, Blueprint # Importa as classes e funções necessárias do Flask
from models import db, Usuario, Produto # Importa o objeto do banco de dados e os modelos de usuário e produto definidos em models.py

# Importa todas as rotas relacionadas ao cadastro de usuários, login e operações CRUD de produtos
from usuario_cadastro import usuario_cadastro_routes
from usuario_login import usuario_login_routes
from produto_cadastro import cadastrar_routes
from produto_atualizar import atualizar_routes
from produto_excluir import excluir_routes

#Instância do Flask
app = Flask(__name__)

# Registro de blueprints para rotas relacionadas a usuários e produtos
# Cada blueprint agrupa rotas relacionadas para melhor organização do código
app.register_blueprint(usuario_cadastro_routes)
app.register_blueprint(usuario_login_routes)
app.register_blueprint(cadastrar_routes)
app.register_blueprint(atualizar_routes)
app.register_blueprint(excluir_routes)

# Configuração da URI do banco de dados SQLAlchemy, desativação do rastreamento de modificações e definição da chave secreta para o Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/S4_Suprimentos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 's4_suprimentos'

# Rota para redirecionar para a página de login/cadastro
@app.route('/')
def redirecionar_para_index():
    return redirect(url_for('pagina_cadastro_login'))

# Rota para renderizar a página de login/cadastro
@app.route("/s4_suprimentos_cadastro_login")
def pagina_cadastro_login():
    return render_template("pagina_login_cadastro.html")

# Rota para a página inicial, com a função READ e DELETE para uma página só
@app.route("/index")
def index():
    produtos = Produto.query.all()
    return render_template("index.html", produtos=produtos)

if __name__ == '__main__':
    db.init_app(app=app) # Inicializa o banco de dados SQLAlchemy associado à aplicação Flask
    app.run(host='localhost', debug=True) # Inicia o servidor Flask em modo de depuração
