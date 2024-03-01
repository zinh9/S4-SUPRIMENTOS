from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, Blueprint
from models import db
from flask_login import LoginManager, login_user, login_required

from usuario_cadastro import usuario_cadastro_routes
from usuario_login import usuario_login_routes
from produto_cadastro import cadastrar_routes
from produto_listar import listar_routes
from produto_atualizar import atualizar_routes
from produto_excluir import excluir_routes

app = Flask(__name__)

app.register_blueprint(usuario_cadastro_routes)
app.register_blueprint(usuario_login_routes)
app.register_blueprint(cadastrar_routes)
app.register_blueprint(listar_routes)
app.register_blueprint(atualizar_routes)
app.register_blueprint(excluir_routes)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/S4_Suprimentos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 's4_suprimentos'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(idUsuario):
    return Usuario.query.get(int(idUsuario))

@app.route('/')
def redirecionar_para_index():
    return redirect(url_for('pagina_cadastro_login'))

@app.route("/s4_suprimentos_cadastro_login")
def pagina_cadastro_login():
    return render_template("pagina_login_cadastro.html")

@app.route("/index")
@login_required
def index():
    return render_template("index.html")

if __name__ == '__main__':
    db.init_app(app=app)
    app.run(host='localhost', debug=True)
