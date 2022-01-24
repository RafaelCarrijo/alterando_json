from flask import request, jsonify, render_template
from app.controlers.operator_json import change_json
from app import app


#Controle de páginas
@app.route('/count_vowel', methods=["GET", "POST"])
def count_str():

    if request.method == "POST":
    #Recebe uma string e conta as vogais com o metodo do controler operator_json

        string = request.form['string']
        validation_string = any(chr.isdigit() for chr in string)

        #Caso indentifique pelo menos um numero no input, vai redirecionar para a pagina de erro.
        if validation_string:
            return render_template('error.html')

        make_json = change_json(string)
        new_json = jsonify(make_json)

        return new_json
    else:
        return 'Metodo "POST", nao foi encontrado'


@app.route('/')
def index():
    return render_template('index.html')