from flask import Flask, render_template, jsonify
from model import Computador
import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


uname = platform.uname()
nome = uname.node
svmem = psutil.virtual_memory()
memoria_total = get_size(svmem.total)
memoria_em_uso = get_size(svmem.used)
memoria_disponivel = get_size(svmem.available)

computador = Computador(nome, memoria_total,
                        memoria_em_uso, memoria_disponivel)

app = Flask(__name__)


computador_dicionario = computador.__dict__


@app.route('/')
def index():
    return render_template('index.html', computador=computador)


@app.route('/api')
def api():
    return jsonify(computador_dicionario)


app.run(debug=True)
