# Dever do controlador coletar os dados e mandar para o backend, o front deve estar limpo!
from models.cliente import Cliente

# Só def
from flask import request


def adicionar_cliente():
    # Dever do controlador é adquirir dados e mandar para o backend
    # Adquirir dados
    nome1 = request.form.get('name')
    email1 = request.form.get('email')
    # Bandando pro back
    # Executando função!
    Cliente.adicionar_cliente(nome1,email1)

def buscar_clientes():
    # Solicitou ao backend a lista:
    lista_clientes = Cliente.buscar_clientes()
    # Retornar a lista para o front poder usa-la
    return lista_clientes
    

