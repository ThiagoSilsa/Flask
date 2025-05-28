from flask import Flask
from routes.rotas import home_route,tabela_route


app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(tabela_route)

app.run(debug=True)

# Esse trecho garante que o arquivo só seja executado quando o arquivo for usado diretamente
# E não importado como módulo
if __name__ == '__main__':
    app.run(debug=True)