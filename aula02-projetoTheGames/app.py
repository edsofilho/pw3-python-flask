from flask import Flask
from controllers import routes
#importando pacote do flask

app = Flask (__name__, template_folder='views') #carregando flask na variável app

routes.init_app(app)

if __name__ == '__main__': #rodando o servidor no localhost, porta 5000
    app.run(host = 'localhost', port=5000, debug = True)
