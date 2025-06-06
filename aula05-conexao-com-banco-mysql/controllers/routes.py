from flask import render_template, request, redirect, url_for
from models.database import Game, db

# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5', 'Jogo 6']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)

    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título': request.form.get('titulo'), 'Ano': request.form.get(
                    'ano'), 'Categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/<int:id>', methods=['GET', 'POST'])
    def estoque(id=None):
        # Se o id for passado na rota, então é para excluir
        if request.method == 'GET' and id:
            game = Game.query.get(id)
            if game:
                db.session.delete(game)
                db.session.commit()
            return redirect(url_for('estoque'))

        # Se for edição (o campo oculto "id" vem preenchido)
        if request.method == 'POST' and request.form.get('id'):
            game = Game.query.get(int(request.form['id']))
            if game:
                game.titulo = request.form['titulo']
                game.ano = request.form['ano']
                game.categoria = request.form['categoria']
                game.plataforma = request.form['plataforma']
                game.preco = request.form['preco']
                db.session.commit()
            return redirect(url_for('estoque'))

        # Se for cadastro (sem campo "id")
        if request.method == 'POST':
            newgame = Game(request.form['titulo'], request.form['ano'],
                        request.form['categoria'], request.form['plataforma'], request.form['preco'])
            db.session.add(newgame)
            db.session.commit()
            return redirect(url_for('estoque'))

        # Exibe os jogos na tabela
        gamesEmEstoque = Game.query.all()
        id_editar = request.args.get('edit_id', None)
        if id_editar:
            id_editar = int(id_editar)
        return render_template('estoque.html', gamesEmEstoque=gamesEmEstoque, id_editar=id_editar)
    
