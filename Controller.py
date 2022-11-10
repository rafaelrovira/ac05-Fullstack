from flask import Flask, redirect, render_template
from flask_mysqldb import MySQL
import Model_Connection



# Configs
app = Flask(__name__)

# Conexão com o banco
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'bancodeteste'
mysql = MySQL(app)


# Rotas
@app.route('/')
def home():
    return "Acessar a rota /cliente"


@app.route('/cliente')
def cliente():
    cadastro_email = Model_Connection.ClienteModel.cadastrarEmail()
    print(cadastro_email)
    return "Email cadastrado com sucesso, verificar console python"


# Main
if __name__ == '__main__':
    app.run(debug=True,port= 5000)