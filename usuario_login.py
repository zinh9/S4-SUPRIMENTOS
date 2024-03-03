# Arquivo para fazer login de usuário na plataforma 

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Usuario

# Blueprint para as rotas de login de usuários
usuario_login_routes = Blueprint('usuario_login_routes', __name__)

# Rota para login de usuários
@usuario_login_routes.route("/login", methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")

        if email and senha:
            # Verifica se o email do usuário existe no banco de dados
            usuario = Usuario.query.filter_by(email=email).first()

            if usuario and usuario.senha == senha:
                # Se o email e senha forem validados, redireciona para a página principal
                return redirect(url_for("index"))
            
            else:
                # Se as crecências forem invalidas, uma mensagem será exibida
                flash('Credenciais inválidas. Tente novamente.', 'error')
        
        else:
            # Se algum campo não for preenchido corretamente, uma mensagem será exibida
            flash('Por favor, preencha todos os campos.', 'error')

    # Renderiza o template do formulário de login de usuário
    return render_template("login_usuario.html")