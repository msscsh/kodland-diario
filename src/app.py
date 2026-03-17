from flask import Flask, flash, redirect, url_for, render_template
from flask_login import LoginManager, login_required, current_user
from model.user import User
from routes.auth import auth as auth_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '5010169f-f5ff-43d8-bc0a-aea4d32f09fa'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Por favor realize o login."
login_manager.login_message_category = "info"

app.register_blueprint(auth_blueprint)

@app.route('/')
@login_required
def home():
    return render_template('index.html', usuario=current_user)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    flash("Por favor realize o login.")
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)