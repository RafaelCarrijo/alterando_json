from flask import Flask, request, jsonify, render_template
from controlers.operator_json import change_json

app = Flask(__name__, static_folder='templates')

@app.route('/count_vowel', methods=["GET", "POST"])
def count_str():

    if request.method == "POST":
    #recebe uma string e conta as vogais com o metodo do controler operator_json

        string = request.form['string']
        validation_string = any(chr.isdigit() for chr in string)

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

if __name__ == '__main__':
    app.run(debug=True)

