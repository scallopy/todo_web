import sys
from flask import Flask, render_template, request, redirect, url_for
import main as func

app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add_todo():
    s = request.form.get("title")
    func.addTodo(s)
    return redirect(url_for("home"))


@app.route('/', methods=["GET"])
def home():
    content = func.lsTodo()
    return render_template('index.html', content=content)


# Function to complete a todo
@app.route("/done/<int:no>", methods=["GET", "POST"])
def done(no):
    func.completeTodo(no)
    return redirect(url_for("report"))


@app.route("/edit/<int:no>")
def edit(no):
    todos = func.read_todos_from_db()
    no = int(no) - 1
    with open("todo.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line == todos[no]:
                new_line = line
    return render_template("update.html", line=new_line, no=(no+1))


@app.route("/update/<int:no>", methods=["POST"])
def update_todo(no):
    todos = func.read_todos_from_db()
    new_item = request.form.get("title")
    func.updateTodo(no, new_item)
    return redirect(url_for("home"))


@app.route("/delete/<int:no>", methods=["GET"])
def delete(no):
    func.deleteTodo(no)
    return redirect(url_for("home"))


# Function to show report/statistics of todo list
@app.route('/report', methods=["GET"])
def report():
    try:
        content = func.reportCompletedTodo()
        return render_template(
            'report.html', content=content)

    except Exception:
        content = {"cont": "There are not completed todos!"}
        return render_template(
            'report.html', content=content)


def main(argv):
    reloader = True
    print('Starting with reloader={}'.format(reloader))
    app.run(port=8080, debug=True, use_reloader=reloader)


if __name__ == "__main__":
    main(sys.argv)
