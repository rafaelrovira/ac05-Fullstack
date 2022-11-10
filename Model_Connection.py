import json
from Controller import mysql



class ClienteModel():


    def cadastrarEmail():

        nome = 'Alexandre'
        email = 'aaaa@aaaa.com'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes VALUES(%s,%s)''',(nome,email))
        mysql.connection.commit()
        cursor.close()
        return 'Criado com sucesso'


    def atualizar():
        #regra de negocio
        #Banco de dados e atualizando os dados
        return 'Atualizado com sucesso'


ClienteModel.cadastrarEmail()