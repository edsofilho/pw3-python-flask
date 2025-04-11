# Comentário em Python
# Importando o pacote do Flask
from flask import Flask, render_template
# importando o MySQL
import pymysql
# Importando as rotas dos controlers
from controllers import routes
# Importando o models
from models.database import db

#Carregamoento da variável app
app = Flask(__name__, template_folder='views')

#Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

# Define o nome do banco de dados
DB_NAME = 'games'

# Configura o flask com o banco definido
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:admin@localhost/{DB_NAME}'

#Iniciando o servidor no localhost,porta 5000, modo de depuração ativado
if __name__ == '__main__':
    # Criando os dados de conexão
    conection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                charset='utf8mb4',
                                cursorclass='pymysql.cursors.DictCursor')
    # Tentado criar o banco
    # Try, trata o sucesso
    try:
        # with cria um recurso temporariamente
        with conection.cursor() as cursor:
            # Cria o banco de dados (se ele não existir)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados {DB_NAME} está criado")
        
    # Except, trata a falha
    except Exception as e:
        print(f"erro ao criar o banco de dados: {e}")
    finally:
        conection.close()
    # Passando a aplicação SQLAlchemy
    db.init_app(app=app)
    # Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
    # Inicializando a aplicação Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
