from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id
    
    @staticmethod
    def get(nome):
        if nome == "admin":
            return User(nome)
        return None