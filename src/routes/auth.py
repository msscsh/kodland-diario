from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from model.educador import Educador
from model.estudante import Estudante

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id_do_educador = request.form.get('usuario')
        senha = request.form.get('senha')
        if (id_do_educador == 'girafales' and senha == 'girafales') or (id_do_educador == 'pardal' and senha == 'pardal') :
            educador = Educador.get(id_do_educador) 
            login_user(educador)
            estudantes = Estudante.listar_todos()
            return render_template('index.html', educador=current_user, estudantes=estudantes)
        else:
            flash('Credenciais incorretas')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


