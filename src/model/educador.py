from flask_login import UserMixin

class Educador(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = 'Professor ' + nome
    
    @staticmethod
    def get(id):
        educadores = {
            "girafales": {"nome": "Girafales", "senha": "girafales"},
            "pardal": {"nome": "Pardal", "senha": "pardal"}
        }
        if id in educadores:
            dados = educadores[id]
            return Educador(id=id, nome=dados["nome"])
        return None