import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT UNIQUE,
        senha TEXT
    )
''')
conn.commit()

def cadastrar():
    print("=== Cadastro de Usuário ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    confirmar_senha = input("Confirme sua senha: ")

    if senha != confirmar_senha:
        print("As senhas não coincidem. Tente novamente.")
        return

    # Inserir usuário no banco de dados
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conn.commit()
    print("Cadastro realizado com sucesso!")

def fazer_login():
    print("=== Login ===")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    # Buscar usuário no banco de dados
    cursor.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
    usuario = cursor.fetchone()

    if usuario:
        print("Login bem-sucedido!")
        print(f"Bem-vindo, {usuario[1]}!")
    else:
        print("Email ou senha incorretos.")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            fazer_login()
        elif opcao == "3":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu()

# Fechar conexão com o banco de dados ao final do programa
conn.close()