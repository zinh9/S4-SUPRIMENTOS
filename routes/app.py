from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy


from produto_cadastro import cadastrar_routes
from produto_listar import listar_routes
from produto_atualizar import atualizar_routes
from produto_excluir import excluir_routes

app = Flask(__name__)

app.register_blueprint(cadastrar_routes)
app.register_blueprint(listar_routes)
app.register_blueprint(atualizar_routes)
app.register_blueprint(excluir_routes)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/S4_Suprimentos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 's4_suprimentos'

db = SQLAlchemy(app)

@app.route('/')
def redirecionar_para_index():
    return redirect(url_for('index'))

@app.route("/s4_suprimentos_cadastro_login")
def pagina_cadastro_login():
    return render_template("pagina_login_cadastro.html")

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
