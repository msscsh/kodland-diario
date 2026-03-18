import datetime

hoje = datetime.date.today().isoformat()
ontem = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

estudantes_db = {
    "1": {
        "nome": "Alice Silva",
        "frequencia": [ontem, hoje],
        "anotacoes": [
            [ontem, "Entregou o exercício de lógica."],
            [hoje, "Participou ativamente da discussão sobre Flask."]
        ]
    },
    "2": {
        "nome": "João Souza",
        "frequencia": [ontem],
        "anotacoes": [
            [ontem, "Demonstrou dificuldade com Blueprints."]
        ]
    },
    "3": {
        "nome": "Maria Oliveira",
        "frequencia": [hoje],
        "anotacoes": [
            [hoje, "Solicitou material extra sobre Jinja2."]
        ]
    }
}