from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import DECIMAL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/S4_Suprimentos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 's4_suprimentos'

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'

    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

class Produto(db.Model):
    __tablename__ = 'produto'

    idProduto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    valor = db.Column(DECIMAL(precision=10, scale=2))

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

@app.route('/')
def redirecionar_para_index():
    return redirect(url_for('index'))

@app.route("/s4_suprimentos_cadastro_login")
def pagina_cadastro_login():
    return render_template("pagina_login_cadastro.html")

@app.route("/cadastro-usuario", methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")

        if email and senha:
            usuario_existente = Usuario.query.filter_by(email=email).first()

            if usuario_existente:
                flash('Este e-mail já está em uso. Por favor, escolha outro.', 'error')
                return redirect(url_for("pagina_cadastro_login"))

            novo_usuario = Usuario(email, senha)

            db.session.add(novo_usuario)
            db.session.commit()
    
            return redirect(url_for("pagina_cadastro_login"))
    
    return render_template("cadastro_usuario.html")


@app.route("/login", methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")

        if email and senha:
            usuario = Usuario.query.filter_by(email=email).first()

            if usuario and usuario.senha == senha:
                return redirect(url_for("index"))
            
            else:
                flash('Credenciais inválidas. Tente novamente.', 'error')
        
        else:
            flash('Por favor, preencha todos os campos.', 'error')

    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
