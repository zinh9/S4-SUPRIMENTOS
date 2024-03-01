from flask import Blueprint, render_template, request, redirect, url_for
from models import Usuario
from app import db

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