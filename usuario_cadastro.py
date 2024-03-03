# Arquivo para cadastrar um novo usuário na plataforma

from flask import Blueprint, render_template, request, redirect, url_for, flash 
from models import db, Usuario # Importa o objeto do banco de dados e os modelos de usuario definidos em models.py

# Blueprint para as rotas de cadastro de usuários
usuario_cadastro_routes = Blueprint('usuario_cadastro', __name__)

# Rota para o cadastro de usuários
@usuario_cadastro_routes.route("/cadastro-usuario", methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")

        if email and senha:
            # Verifica se o e-mail já está em uso
            usuario_existente = Usuario.query.filter_by(email=email).first()

            if usuario_existente:
                # Exibe mensagem de erro se o e-mail já estiver em uso
                flash('Este e-mail já está em uso. Por favor, escolha outro.', 'error')
                return redirect(url_for("pagina_cadastro_login"))

            # Cria um novo usuário e adiciona ao banco de dados
            novo_usuario = Usuario(email, senha)
            db.session.add(novo_usuario)
            db.session.commit()
    
            # Redireciona para a página de login/cadastro após o cadastro bem-sucedido
            return redirect(url_for("pagina_cadastro_login"))
        
    # Renderiza o template do formulário de cadastro de usuário
    return render_template("cadastro_usuario.html")