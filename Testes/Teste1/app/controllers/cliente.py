# Dever do controlador coletar os dados e mandar para o backend, o front deve estar limpo!
from models.cliente import Cliente

# Só def
from flask import request


def adicionar_cliente():
    # Dever do controlador é adquirir dados e mandar para o backend
    # Adquirir dados
    nome = request.form.get('name')
    email = request.form.get('email')
    # Bandando pro back
    novo_usu = Cliente(nome, email)
    # Executando função!
    novo_usu.adicionar_cliente()

