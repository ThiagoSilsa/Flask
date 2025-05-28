# Rotas apenas dos clientes

from flask import Blueprint, render_template, request

# Importanto simulaçao de banco de dados
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

# Render_template irá sempre buscar na pasta "templates" de acordo com a posição do arquivo principal,
# nesse caso o "main.py"


@cliente_route.route('/')
def lista_clientes():
    """Listar o cliente"""
    return render_template('lista_clientes.html', clientes=CLIENTES)
# Enviei a var clientes para o html


@cliente_route.route('/new', methods=['GET'])
def form_novo_cliente():
    """
        Formulário para cadastrar cliente
    """
    return render_template('form_cliente.html')


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """
        Inserir os dados do cliente
    """
    # Interceptando dados
    data = request.json

    novo_usuario ={
        "id": len(CLIENTES) + 1,
        "name" : data['name'],
        "email" : data['email']
    }
    CLIENTES.append(novo_usuario)
    return {'ok': 'ok'}


@cliente_route.route('/<int:cliente_id>', methods=['GET'])
def detalhe_cliente(cliente_id):
    """
        Exibir detalhes do cliente
    """
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit', methods=['GET'])
def form_editar_cliente(cliente_id):
    """
        Formulario para editar cliente
    """
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """
        Atualizar dados do cliente
    """
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """
        Deletar cliente
    """
    pass
