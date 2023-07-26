# models.py
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do SQLAlchemy
db = SQLAlchemy()

# Classe para representar a tabela "contato"
class Contato(db.Model):
    __tablename__ = 'contato'
    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100))
    Sobrenome = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Telefone = db.Column(db.String(20))

    def __init__(self, nome, sobrenome, email, telefone):
        self.Nome = nome
        self.Sobrenome = sobrenome
        self.Email = email
        self.Telefone = telefone
