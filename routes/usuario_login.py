from flask import Blueprint, render_template, request, redirect, url_for
from models import Usuario
from app import db

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
