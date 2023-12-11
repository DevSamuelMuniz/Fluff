from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="usuario" 
)

@app.route('/data_from_mysql', methods=['GET'])
def get_data_from_mysql():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM sua_tabela')
    data = cursor.fetchall()
    cursor.close()
    return jsonify({'data_from_mysql': data})

if __name__ == '__main__':
    app.run(debug=True)