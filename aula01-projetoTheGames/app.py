# Importando o pacote Flask
from flask import Flask, render_template

# Carregando o Flask  na variavel app
app = Flask(__name__, template_folder='views')

# criando a rota principal do site


@app.route('/')
# Criando função no python
# View function - Função de visualisação
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    # Dicionário no Python (objeto)
    game = {'Titulo': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'}

    jogadores = ['edsonGF', 'davi_lambari', 'iruah']
    jogos = ['Minecraft', 'Fortnite', 'League of Legends',
             'Croosfire', 'Free Fire', 'Roblox', 'Call of Duty']


    return render_template('games.html',
                       game=game,
                       jogadores=jogadores)


if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
