# Rotas apenas da página principal!

from flask import Blueprint, render_template

# Grupo de urls para página principal

# var com o nome e _route = Blueprint'nome do grupo'
home_route = Blueprint('home', __name__)

# Primeira rota:
@home_route.route('/')
def home():
    return render_template('index.html')