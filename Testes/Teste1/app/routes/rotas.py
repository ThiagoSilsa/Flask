# Aqui seria como se fosse a View.
# Logo, devo enviar solicitações ao controler!!

from flask import Blueprint, render_template,request

# Imporanto o "banco de dados":
from database.database import CLIENTES



home_route = Blueprint('home', __name__)
tabela_route = Blueprint('tabela',__name__)


@home_route.route('/', methods = ['GET','POST'])
def home():
    if request.method == "POST":
        # Aqui chamaria o controlador para acessar o backend.
        from controllers.cliente import adicionar_cliente
        adicionar_cliente()

    return render_template("index.html")

@tabela_route.route('/tabela', methods=['GET'])
def tabela():
    # enviando a tabela clientes para a tabela
    return render_template('tabela.html', clientes = CLIENTES)