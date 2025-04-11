from flask import render_template, request
jogadores=['iruah', 'davi_lambari', 'edsongf1', 'kioto','black_butterfly', 'jujudopix']
gamelist=[{'Título' :'CS-GO', 'Ano': 2012, 'Categoria' : 'FPS online'}]
        
def init_app(app):
    @app.route('/')
#criando função no python
    def home():
        return render_template('index.html')

    @app.route('/games', methods = ['GET','POST'])
#criando função no python
    def games():
        game= gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                           game = game,
                           jogadores=jogadores,)
    @app.route('/cadGames', methods = ['GET','POST'])
    def cadGames():
        return render_template('cadGames.html',
        gamelist = gamelist)