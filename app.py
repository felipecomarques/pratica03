from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html",\
        titulo_pagina="Pagina inicial")

@app.route('/sobre')
def sobre():
    return render_template("paginas/sobre.html",\
        titulo_pagina="Sobre o site")

@app.route('/carrinho')
def cart():
    return render_template("paginas/carrinho.html",\
        titulo_pagina="Carrinho")

@app.route('/novidade')
def novidade():
    return render_template("paginas/novidades.html",\
        titulo_pagina="Novidades!")

@app.route('/promocoes')
def promocoes():
    return render_template("paginas/promocoes.html",\
        titulo_pagina="Promocoes")

if __name__ == "__main__":
    app.run(debug=True)