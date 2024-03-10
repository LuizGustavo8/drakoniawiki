from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Arcos

@app.route('/A_Ambicao_de_Uhm')
def ambicao_de_uhm():
    return render_template('A_Ambicao_de_Uhm.html')

@app.route('/A_Justica_dos_Famintos')
def justica_dos_famintos():
    return render_template('A_Justica_dos_Famintos.html')

@app.route('/A_Lenda_de_Yamahachi')
def lenda_de_yamahachi():
    return render_template('A_Lenda_de_Yamahachi.html')

@app.route('/A_Semana_de_Arte')
def semana_de_arte():
    return render_template('A_Semana_de_Arte.html')

@app.route('/As_Profundezas_do_Conhecimento')
def profundezas_do_conhecimento():
    return render_template('As_Profundezas_do_Conhecimento.html')

@app.route('/O_Resgate_do_Diplomata')
def resgate_do_diplomata():
    return render_template('O_Resgate_do_Diplomata.html')

@app.route('/O_Banquete_Vermelho')
def banquete_vermelho():
    return render_template('O_Banquete_Vermelho.html')

@app.route('/APOCALIPSE_I')
def apocalipse_um():
    return render_template('APOCALIPSE_I.html.html')

#Personagens

@app.route('/Melchior_Vergullion')
def melchior_vergullion():
    return render_template('Melchior_Vergullion.html')

@app.route('/Harubin')
def harubin():
    return render_template('Harubin.html')

@app.route('/Lekko')
def lekko():
    return render_template('Lekko.html')

@app.route('/Thiagao')
def thiagao():
    return render_template('Thiagao.html')

@app.route('/Torgrut')
def torgrut():
    return render_template('Torgrut.html')

@app.route('/Night')
def night():
    return render_template('Night.html')

@app.route('/Tauraa')
def tauraa():
    return render_template('Tauraa.html')

#O Mundo

@app.route('/Deuses')
def deuses():
    return render_template('Deuses.html')

@app.route('/Nacoes')
def nacoes():
    return render_template('Nacoes.html')

@app.route('/Guerras_Runicas')
def guerras_runicas():
    return render_template('Guerras_Runicas.html')

@app.route('/Conhecimentos_Gerais')
def conhecimentos_gerais():
    return render_template('Conhecimentos_Gerais.html')


#One-Shots

@app.route('/Wesnoth')
def wesnoth():
    return render_template('Wesnoth.html')

@app.route('/Belier')
def belier():
    return render_template('Belier.html')

@app.route('/Terror_Pristino')
def terror_pristino():
    return render_template('Terror_Pristino.html')


if __name__ == '__main__':
    app.run(debug=True)
