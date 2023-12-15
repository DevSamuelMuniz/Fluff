from flask import Flask, redirect, jsonify, render_template, request, session, url_for
import mysql.connector
import base64

app = Flask(__name__)

app.secret_key = '7aBd&k0dldP9X3sasZ'

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

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/upload_form')
def upload_form():
    return render_template('upload.html')


@app.route('/feed')
def feed():
    return render_template('feed.html')


@app.route('/cards', methods=['GET', 'POST'])
def login():
    mensagem = None

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        cursor = db.cursor()
        sql = "SELECT nome FROM usuario WHERE email = %s AND senha = %s"
        cursor.execute(sql, (email, senha))
        user = cursor.fetchone()

        if user:
            session['logged_in'] = True
            session['nome_usuario'] = user[0] 
            session['email'] = email  
            return render_template('cards.html')

        else:
            mensagem = "Credenciais inválidas. Tente novamente."

    return render_template('index.html', mensagem=mensagem)


@app.route('/get_posts/<int:imagem>')
def get_posts(imagem):
    cursor = db.cursor()
    sql = "SELECT imagem, titulo, descricao FROM posts"
    cursor.execute(sql)
    posts = cursor.fetchall()
    cursor.close()

    posts_with_base64 = []
    for post in posts:
        imagem_base64 = base64.b64encode(post['imagem']).decode('utf-8') if post['imagem'] else None
        post_dict = {
            'imagem': imagem_base64,
            'titulo': post['titulo'],
            'descricao': post['descricao']
        }
        posts_with_base64.append(post_dict)

    return jsonify(posts_with_base64)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('nome_usuario', None)
    return redirect(url_for('index'))

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        data = request.form 
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        cursor = db.cursor()
        sql = "SELECT * FROM usuario WHERE email = %s"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()

        if result:
            mensagem = "Email já cadastrado. Tente com outro email."
            return render_template('registro.html', mensagem=mensagem)
        else:
            cursor = db.cursor()
            sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
            val = (nome, email, senha)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()

    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()  

    if 'imageData' in data and 'titulo' in data and 'descricao' in data:
        imagem = data['imageData']  
        titulo = data['titulo']  
        descricao = data['descricao']  

        cursor = db.cursor()
        sql = "INSERT INTO posts (titulo, descricao, imagem) VALUES (%s, %s, %s)"
        cursor.execute(sql, (titulo, descricao, imagem))
        db.commit()
        cursor.close()

        return render_template('cards.html')
    else:
        return jsonify({'error': 'Dados incompletos ou ausentes.'}), 400


@app.route('/card')
def card():
    cursor = db.cursor()
    sql = "SELECT TO_BASE64(imagem) AS imagem_base64, titulo, descricao FROM posts"
    cursor.execute(sql)
    posts = cursor.fetchall()
    cursor.close()

    posts_with_base64 = []
    for post in posts:
        imagem_base64 = post[0] if post[0] else None
        post_dict = {
            'imagem': imagem_base64,
            'titulo': post[1],
            'descricao': post[2]
        }
        posts_with_base64.append(post_dict)

    return render_template('cards.html', posts=posts_with_base64)


@app.route('/mudar', methods=['GET', 'POST'])
def mudar():
    mensagem = None

    if request.method == 'POST':
        nova_senha = request.form.get('nova_senha')
        confirmar_nova_senha = request.form.get('confirmar_nova_senha')

        if nova_senha == confirmar_nova_senha:
            email_usuario = session.get('email')

            cursor = db.cursor()
            sql = "UPDATE usuario SET senha = %s WHERE email = %s"
            cursor.execute(sql, (nova_senha, email_usuario))
            db.commit()
            cursor.close()

            mensagem = "Senha alterada com sucesso!"
        else:
            mensagem = "As senhas não coincidem. Tente novamente."

    return render_template('mudar.html', mensagem=mensagem)

@app.route('/apagar', methods=['GET', 'POST'])
def apagar():
    mensagem = None

    if request.method == 'POST':
        senha_confirmacao = request.form.get('nova_senha')

        email_usuario = session.get('email')

        cursor = db.cursor()
        sql = "SELECT nome FROM usuario WHERE email = %s AND senha = %s"
        cursor.execute(sql, (email_usuario, senha_confirmacao))
        user = cursor.fetchone()

        if user:
            delete_sql = "DELETE FROM usuario WHERE email = %s"
            cursor.execute(delete_sql, (email_usuario,))
            db.commit()
            cursor.close()

            mensagem = "Sua conta foi excluída com sucesso!"
            session.pop('logged_in', None)
            session.pop('nome_usuario', None)
            session.pop('email', None)
            return redirect(url_for('index'))
        else:
            mensagem = "Senha de confirmação incorreta. Tente novamente."

    return render_template('apagar.html', mensagem=mensagem)




if __name__ == '__main__':
    app.run(debug=True)