from flask import Flask

# Importando a variável da rota
from routes.home import home_route
from routes.cliente import cliente_route

# Iniciando flask
app = Flask(__name__)

# Registrando a variável
app.register_blueprint(home_route)

# Tenho que informar qual o prefixo da url
app.register_blueprint(cliente_route, url_prefix = '/cliente')

app.run(debug=True)