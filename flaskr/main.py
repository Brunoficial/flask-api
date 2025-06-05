from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

usuarios = [
    {
        "id": 1,
        "nome": "Bruno",
        "mensagem": "Eu sou Bruno, duhh"
    },
    {
        "id": 2,
        "nome": "Caua",
        "mensagem": "Eu sei programar"
    }
]


@app.route("/users", methods=["GET", "POST"])
def retornarUsuarios():
    return (
        jsonify(usuarios)
    )

@app.route("/users/<int:usuario_id>", methods=["GET"])
def retornarUsuario(usuario_id):
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        return jsonify({"message": "Usuario com esse id não encontrado"}), 404
    return jsonify(usuario)

@app.route("/users/create", methods=["POST"])
def criarUsuario():
    id = uuid.uuid4()
    data = request.get_json()

    novoUsuario = {
        "id": id,
        "nome" : data.get("nome"), 
        "mensagem" : data.get("mensagem")
    }

    usuarios.append(novoUsuario)
    return jsonify(usuarios)

@app.route("/users/delete/<int:id>", methods=['DELETE'])
def deletarUsuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)

    return usuarios

@app.route("/users/edit/<int:id>", methods=['PATCH'])
def editarUsuario(id):
    data = request.get_json()
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = data["nome"]
            usuario["mensagem"] = data["mensagem"]

    return usuarios
