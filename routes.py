from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import db, Contato

app = Flask(__name__)

#Configuração do banco de dados
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'senha123'
app.config['MYSQL_DB'] = 'agenda'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senha123@localhost/agenda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)
db.init_app(app)
engine = create_engine('mysql://root:senha123@localhost/agenda')
Session = sessionmaker(bind=engine)

@app.route('/contato', methods=['POST'])
def create_contato():
    if request.method == 'POST':
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        email = request.json['email']
        telefone = request.json['telefone']

        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO contato (Nome, Sobrenome, Email, Telefone) VALUES (%s, %s, %s, %s)',
            (nome, sobrenome, email, telefone)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Contato criado com sucesso'}), 201

@app.route('/contato/<int:id>', methods=['GET'])
def get_contato(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contato WHERE ID = %s', (id,))
    contato = cur.fetchone()
    cur.close()

    if contato:
        return jsonify(contato), 200
    else:
        return jsonify({'message': 'Contato não encontrado'}), 404

@app.route('/contato/<int:id>', methods=['PUT'])
def update_contato(id):
    if request.method == 'PUT':
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        email = request.json['email']
        telefone = request.json['telefone']

        cur = mysql.connection.cursor()
        cur.execute(
            'UPDATE contato SET Nome = %s, Sobrenome = %s, Email = %s, Telefone = %s WHERE ID = %s',
            (nome, sobrenome, email, telefone, id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Contato atualizado com sucesso'}), 200

@app.route('/contato/<int:id>', methods=['DELETE'])
def delete_contato(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contato WHERE ID = %s', (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Contato deletado com sucesso'}), 200

@app.route('/contato/search', methods=['GET'])
def search_contatos():
    # Obtenhe os parâmetros de consulta da URL
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    email = request.args.get('email')
    telefone = request.args.get('telefone')

    query = Contato.query

    if nome:
        query = query.filter(Contato.Nome.ilike(f"%{nome}%"))
    if sobrenome:
        query = query.filter(Contato.Sobrenome.ilike(f"%{sobrenome}%"))
    if email:
        query = query.filter(Contato.Email.ilike(f"%{email}%"))
    if telefone:
        query = query.filter(Contato.Telefone.ilike(f"%{telefone}%"))

    contatos = query.all()

    if not contatos:
        return jsonify({'message': 'Nenhum contato encontrado para os critérios de pesquisa fornecidos.', 'status': 'success'}), 200

    contatos_json = []
    for contato in contatos:
        contato_dict = {
            'ID': contato.ID,
            'Nome': contato.Nome,
            'Sobrenome': contato.Sobrenome,
            'Email': contato.Email,
            'Telefone': contato.Telefone
        }
        contatos_json.append(contato_dict)

    return jsonify(contatos_json), 200

if __name__ == '__main__':
    app.run(debug=True)
