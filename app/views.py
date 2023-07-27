from flask import request, jsonify
from app import app, db
from app.models import Contato

@app.route('/contato', methods=['POST'])
def create_contato():
    if request.method == 'POST':
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        email = request.json['email']
        telefone = request.json['telefone']

        contato = Contato(nome, sobrenome, email, telefone)
        db.session.add(contato)
        db.session.commit()

        return jsonify({'message': 'Contato criado com sucesso'}), 201

@app.route('/contato/<int:id>', methods=['GET'])
def get_contato(id):
    contato = Contato.query.get(id)

    if contato:
        return jsonify({
            'ID': contato.ID,
            'Nome': contato.Nome,
            'Sobrenome': contato.Sobrenome,
            'Email': contato.Email,
            'Telefone': contato.Telefone
        }), 200
    else:
        return jsonify({'message': 'Contato não encontrado'}), 404

@app.route('/contato/<int:id>', methods=['PUT'])
def update_contato(id):
    if request.method == 'PUT':
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        email = request.json['email']
        telefone = request.json['telefone']

        contato = Contato.query.get(id)
        if contato:
            contato.Nome = nome
            contato.Sobrenome = sobrenome
            contato.Email = email
            contato.Telefone = telefone
            db.session.commit()

            return jsonify({'message': 'Contato atualizado com sucesso'}), 200
        else:
            return jsonify({'message': 'Contato não encontrado'}), 404

@app.route('/contato/<int:id>', methods=['DELETE'])
def delete_contato(id):
    contato = Contato.query.get(id)
    if contato:
        db.session.delete(contato)
        db.session.commit()

        return jsonify({'message': 'Contato deletado com sucesso'}), 200
    else:
        return jsonify({'message': 'Contato não encontrado'}), 404

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

