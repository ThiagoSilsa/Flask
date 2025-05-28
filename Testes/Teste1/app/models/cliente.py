# Backend POO

# Importando database
from database.database import CLIENTES

class Cliente():
    def __init__(self, nome : str, email : str):
        self.novo_usu = {'nome': nome, 'email':email}
    
    def adicionar_cliente(self):
        CLIENTES.append(self.novo_usu)