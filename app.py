from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando banco de dados em memória
todos = [
    {"id": 1, "task": "Aprender GitHub Actions", "done": False},
    {"id": 2, "task": "Criar pipeline CI/CD", "done": False},
]


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/todos")
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    new_todo = {"id": len(todos) + 1, "task": data.get("task"), "done": False}
    todos.append(new_todo)
    return jsonify(new_todo), 201


if __name__ == "__main__":
    app.run(debug=True)
