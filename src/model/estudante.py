from util.db import estudantes_db

class Estudante:
    def __init__(self, matricula, nome, frequencia=None, anotacoes=None):
        self.matricula = matricula
        self.nome = nome
        self.frequencia = frequencia or []
        self.anotacoes = anotacoes or []

    @staticmethod
    def get(matricula_do_estudante):
        dados_do_estudante_recuperado = estudantes_db.get(matricula_do_estudante)
        if dados_do_estudante_recuperado:
            return Estudante(
                matricula=matricula_do_estudante, 
                nome=dados_do_estudante_recuperado["nome"], 
                frequencia=dados_do_estudante_recuperado["frequencia"], 
                anotacoes=dados_do_estudante_recuperado["anotacoes"]
            )
        return None
    
    @staticmethod
    def listar_todos():
        return [
            Estudante(matricula=matricula, nome=dados["nome"], frequencia=dados["frequencia"], anotacoes=dados["anotacoes"])
            for matricula, dados in estudantes_db.items()
        ]
