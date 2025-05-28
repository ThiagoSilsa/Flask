# Backend POO

# Importando database
from database.database import db, Clientes

class Cliente():
    @staticmethod
    def adicionar_cliente(nome1, email1):
        # novo cliente acessa tabela "Clientes" e adiciona novos clientes com o parâmetro fornecido
        novo_cliente = Clientes.create(nome = nome1, email = email1)

    @staticmethod
    def buscar_clientes():
        # Todos serão recebidos numa lista:
        lista_clientes = Clientes.select()
        # Retornando a lista!
        return lista_clientes