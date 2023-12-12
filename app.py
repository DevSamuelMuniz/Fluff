from flask import Flask, redirect, render_template, request, url_for
import mysql.connector

app = Flask(__name__)

# Estabelece a conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="usuarios"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/cards', methods=['GET', 'POST'])

def cards():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Lógica de verificação de login no banco de dados
        cursor = db.cursor()
        sql = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
        cursor.execute(sql, (email, senha))
        user = cursor.fetchone()  # Retorna o primeiro registro encontrado

        if user:
            # Se as credenciais estiverem corretas, redirecione para a página de cards
            return render_template('cards.html')
        else:
            # Se as credenciais estiverem incorretas, retorne para a página de login com uma mensagem de erro
            mensagem = "Credenciais inválidas. Tente novamente."
            return render_template('index.html', mensagem=mensagem)

    return render_template('cards.html')

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        data = request.form  # Obtém os dados enviados pelo formulário
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        # Verificar se o usuário já está registrado no banco de dados
        cursor = db.cursor()
        sql = "SELECT * FROM usuario WHERE email = %s"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()

        # Se não há registro, insira os dados no banco de dados
        if not result:
            cursor = db.cursor()
            sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
            val = (nome, email, senha)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
