from flask import Flask, render_template, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="usuarios" 
)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para receber os dados POST
@app.route('/cadastro', methods=['POST'])
def cadastra_usuario():
    data = request.get_json()  # Obtém os dados enviados no corpo da solicitação
    nome = data.get('name')
    email = data.get('email')
    senha = data.get('password')

    # Faça o que desejar com esses dados, por exemplo, imprimi-los
    print(f"Nome: {nome}, Email: {email}, Senha: {senha}")

    # Aqui você pode retornar uma resposta se necessário
    return jsonify({'message': 'Dados recebidos com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
