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


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)