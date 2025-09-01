from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
contador_id = 1

# criar rotas

@app.route("/users", methods =['POST'])
def criar_usuario():
    global contador_id
    dados = request.json
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"error": "Dados incorretos é necessario informar nome e email"}), 400
    

    usuario = {
        "id": contador_id,
        "nome": dados["nome"],
        "email": dados["email"]
    }
    users.append(usuario)
    contador_id += 1
    return jsonify(usuario), 201

@app.route("/users", methods =['GET'])
def listar_usuarios():
    return jsonify(users), 200

@app.route("/users/<int:id>", methods =['GET'])
def obter_usuario(id):
    for usuario in users:
        if usuario["id"] == id:
            return jsonify(usuario), 200
    return jsonify({"error": "Usuario nao encontrado"}), 404

@app.route("/users/<int:id>", methods = ['PUT'])
def atualizar_usuario(id):
    dados = request.json
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"error": "Dados incorretos é necessario informar nome e email"}), 400
    for usuario in users:
        if usuario["id"] == id:
            if "nome" in dados:
                usuario["nome"] = dados["nome"]
            if "email" in dados:
                usuario["email"] = dados["email"]
            return jsonify(usuario), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route("/users/<int:id>", methods = ['DELETE'])
def deletar_usuario(id):
    for usuario in users:
        if usuario["id"] == id:
            users.remove(usuario)
            return jsonify({"message": "Usuario deletado com sucesso!"}), 200
    return jsonify({"error": "Usuario nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)