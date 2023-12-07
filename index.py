from flask import Flask, render_template, request, jsonify
import random

#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder="./static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-apostas', methods=['POST'])
def gerar_apostas():
    data = request.json
    # Convertendo os valores para inteiros
    num_apostas = int(data['num_apostas'])
    num_numeros = int(data['num_numeros'])
    apostas = gerar_numeros_apostas(num_apostas, num_numeros)
    return jsonify(apostas)

def gerar_numeros_apostas(num_apostas, num_numeros):
    numeros_disponiveis = list(range(1, 61))
    apostas = []
    for _ in range(num_apostas):
        aposta = sorted(random.sample(numeros_disponiveis, num_numeros))
        apostas.append(aposta)
    return apostas

if __name__ == '__main__':
    app.run(debug=True)
