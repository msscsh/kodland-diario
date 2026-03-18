from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from model.estudante import Estudante
from util.db import estudantes_db
import datetime

gestao = Blueprint('gestao', __name__, url_prefix='/gestao')

@gestao.route('/estudante/<matricula_do_estudante>')
def recuperar_dados_do_estudante(matricula_do_estudante):
    if (matricula_do_estudante) :
        estudante = Estudante.get(matricula_do_estudante) 
        if (estudante) :
            eventos_presenca = [{"title": "", "start": data, "allDay": True, "classNames": 'insignia-presenca', "description": 'Presente em sala'} for data in estudante.frequencia]
            eventos_anotacoes = [{"title": "", "start": anotacao[0], "allDay": True, "classNames": 'insignia-anotacao', "description": "Em "+ formatar_data(anotacao[0]) + " o estudante recebeu a seguinte anotação: '" + anotacao[1] + "'"} for anotacao in estudante.anotacoes]
            
            eventos = []
            eventos.extend(eventos_presenca)
            eventos.extend(eventos_anotacoes)

            return render_template('estudante_detalhe.html', estudante=estudante, eventos=eventos)

    flash('Matrícula inexistente ou não informada')
    abort(404)

@gestao.route('/estudante/<matricula_do_estudante>/anotacao', methods=['POST'])
def incluir_anotacao_do_estudante(matricula_do_estudante):
    texto = request.form.get('anotacao')
    hoje = datetime.date.today().isoformat()
    
    if matricula_do_estudante in estudantes_db:
        estudantes_db[matricula_do_estudante]["anotacoes"].append([hoje, texto])
        flash(f'Anotação atribuída ao estudante {estudantes_db[matricula_do_estudante]["nome"]}')
        return redirect(url_for('home', matricula=matricula_do_estudante))

    else:
        flash('Matrícula inexistente ou não informada')
        abort(404)


@gestao.route('/estudante/<matricula_do_estudante>/presenca', methods=['POST'])
def incluir_presenca_do_estudante(matricula_do_estudante):
    if matricula_do_estudante in estudantes_db:
        hoje = datetime.date.today().isoformat()
        if hoje not in estudantes_db[matricula_do_estudante]["frequencia"]:
            estudantes_db[matricula_do_estudante]["frequencia"].append(hoje)
            flash(f'Presença confirmada para o estudante {estudantes_db[matricula_do_estudante]["nome"]}')
        else:
            flash(f'Presença já foi marcada para o estudante {estudantes_db[matricula_do_estudante]["nome"]}')
    
    return redirect(url_for('home', matricula=matricula_do_estudante))

def formatar_data(data_original):
    partes = data_original.split('-')
    return f"{partes[2]}/{partes[1]}/{partes[0]}"