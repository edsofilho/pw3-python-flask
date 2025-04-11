from flask import render_template, request

# Array de objetos
placaslist = [{'Nome': 'Arduino Uno',
               'Codigo': 'A8-009',
               'Valor': '68.99'}]

componenteslist = [{'Nome': 'Led 3v',
               'Codigo': 'A8-009',
               'Categoria': '2.99'}]

sensoreslist = [{'Nome': 'RF',
               'Codigo': 'A8-009',
               'Categoria': '68.99'}]


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
# Criando função no Python
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        return render_template('index.html')

    @app.route('/estoque', methods=['GET', 'POST'])
    def estoque():

        return render_template('estoque.html',
                               componenteslist=componenteslist,
                               sensoreslist=sensoreslist,
                               placaslist = placaslist)

    @app.route('/cadplacas', methods=['GET', 'POST'])
    def cadplacas():
        return render_template('cadplacas.html',
                               placaslist = placaslist)

    @app.route('/cadcomponentes', methods=['GET', 'POST'])
    def cadcomponentes():
        return render_template('cadcomponentes.html',
                               componenteslist=componenteslist)
    @app.route('/cadsensores', methods=['GET', 'POST'])
    def cadsensores():
        return render_template('cadsensores.html', sensoreslist=sensoreslist)
