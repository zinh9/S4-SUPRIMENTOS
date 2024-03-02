from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Usuario

usuario_login_routes = Blueprint('usuario_login_routes', __name__)

@usuario_login_routes.route("/login", methods=['GET', 'POST'])
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