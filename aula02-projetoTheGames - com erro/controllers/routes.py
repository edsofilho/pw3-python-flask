from flask import render_template, request

jogadores = ['edsonGF', 'davi_lambari', 'iruah']
        
        #Array de objetos 
gamelist = [{'Titulo': 'CS-GO',
                'Ano': 2012,
                'Categoria': 'FPS Online'}]

def init_app(app):
    @app.route('/')
    # Criando função no python
    # View function - Função de visualisação
    def home():
        return render_template('index.html')

    @app.route('/games', methods = ['GET', 'POST'])
    # View function
    def games():
        # Dicionário no Python (objeto)
        # Acessando o primeiro jogo da lista de jogos
        game = gamelist[0]

        
        
        if request.method == 'POST':
            if request.form.get('jogador'): #name do input
                jogadores.append(request).form.get('jogador')

        return render_template('games.html',
                                game=games,
                                jogadores=jogadores)
