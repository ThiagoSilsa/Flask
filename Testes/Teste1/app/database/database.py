# Utilizando pewee para conecção com bd
from peewee import *

db = SqliteDatabase('bancodedados.db')

# criando tabela:

class Clientes(Model):
    nome = CharField()
    email = CharField()

    class Meta:
        database = db

# Criando:
# db.create_tables([Clientes])