from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Estabelece a conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="usuarios"
)

# Rota para a página inicial (index.html)
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o arquivo index.html

# Rota para a página de registro (registro.html)
@app.route('/registro')
def registro():
    return render_template('registro.html')


# Rota para receber os dados POST do formulário de registro
@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        data = request.form  # Obtém os dados enviados pelo formulário
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        # Insere os dados no banco de dados
        cursor = db.cursor()
        sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
        val = (nome, email, senha)
        cursor.execute(sql, val)
        db.commit()

        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()

        # Redireciona para a página de registro após cadastrar o usuário
        return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
