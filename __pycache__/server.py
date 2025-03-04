from flask import Flask, request, jsonify
from models import Alunos, Turmas, Professores

app = Flask(__name__)

alunos_db = [
    Alunos(id = 5, nome = "Marcelo", idade = 19)
]

turmas_db = [
    Turmas(id = 3, nome = "3A", professor_id= 8)
]

professores_db = [
    Professores(id = 8, nome = "Caio", disciplina = "Desenvolvimento de Apis")
]

@app.route("/alunos", methods = ["POST"])
def criar_aluno():
     data = request.get_json()
     aluno = Alunos(id = data["id"], nome = data["nome"], idade = data["idade"])
     alunos_db.append(aluno)
     return jsonify(aluno.to_dict()), 201

@app.route("/alunos", methods = ["GET"])
def listar_alunos():
    alunos_list = [aluno.to_dict() for aluno in alunos_db]
    return jsonify(alunos_list), 200


@app.route("/turmas", methods = ["POST"])
def criar_turma():
    data = request.get_json()
    turma = Turmas(id = data["id"], nome = data["nome"], professor_id = data["professor_id"])
    turmas_db.append(turma)
    return jsonify(turma.to_dict()),201

@app.route("/turmas", methods = ["GET"])
def listar_turmas():
    turmas_list = [turma.to_dict() for turma in turmas_db]
    return jsonify(turmas_list), 200

@app.route("/professores", methods = ["POST"])
def criar_professor():
    data = request.get_json()
    professor = Professores(id = data["id"], nome = data["nome"], disciplina = data["disciplina"])
    professores_db.append(professor)
    return jsonify(professor.to_dict()), 201

@app.route("/professores", methods = ["GET"])
def listar_professores():
    professores_list = [professor.to_dict() for professor in professores_db]
    return jsonify(professores_list), 200




if __name__ == "__main__":
    app.run()
    