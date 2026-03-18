from flask import Flask, flash, request, redirect, url_for, render_template
from flask_login import LoginManager, login_required, current_user
from model.educador import Educador
from model.estudante import Estudante
from routes.auth import auth as auth_blueprint
from routes.gestao import gestao as gestao_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '5010169f-f5ff-43d8-bc0a-aea4d32f09fa'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Por favor realize o login."
login_manager.login_message_category = "info"

app.register_blueprint(auth_blueprint)
app.register_blueprint(gestao_blueprint)

@app.route('/')
@login_required
def home():
    estudantes = Estudante.listar_todos()
    matricula_selecionada = request.args.get('matricula')
    return render_template('index.html', educador=current_user, estudantes=estudantes, matricula=matricula_selecionada)

@login_manager.user_loader
def load_user(user_id):
    return Educador.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    flash("Por favor realize o login.")
    return redirect(url_for('auth.login'))

@app.errorhandler(404)
def erro_404(e):
    flash('A rota a qual você tentou acessar não existe')
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)