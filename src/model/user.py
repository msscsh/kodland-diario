from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = 'Professor ' + nome
    
    @staticmethod
    def get(id):
        usuarios = {
            "girafales": {"nome": "Girafales", "senha": "girafales"},
            "pardal": {"nome": "Pardal", "senha": "pardal"}
        }
        if id in usuarios:
            dados = usuarios[id]
            return User(id=id, nome=dados["nome"])
        return None