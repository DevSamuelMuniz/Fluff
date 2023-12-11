import  MySQLdb

con = MySQLdb.connect(host="ServidorMysql", user="UsuarioMysql", passwd="SuaSenha", db="SeuDb")
cursor = con.cursor()
cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))
con.commit()
rs = cursor.fetchone() # busca uma linha
rs = cursor.fetchall() # busca todas as linhas
rs = cursor.dictfetchall() # busca todas as linhas, cada linha tem um dicionário com os nomes dos campos
