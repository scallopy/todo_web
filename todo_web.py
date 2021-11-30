import sys
from flask import Flask, render_template, request, redirect, url_for
import main as func

app = Flask(__name__)


# TODO: Refactor both the web version and the cli version to reuse a common
# set of methods.
#
#              DAO
#       (Data Access Object)
#               |
#         +-----+------+
#         |     |      |
#      WebUI   GUI    CLI
#

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
    try:
        func.completeTodo(no)
        return redirect(url_for("report"))

    except Exception:
        print("Error: todo #{} does not exist. Nothing comleted.".format(no))
        return redirect(url_for("report"))


@app.route("/edit/<int:no>")
def edit(no):
    todos = func.read_todos_from_db()
    no = int(no) - 1
    with open("todo.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line == todos[no]:
                print(line)
                new_line = line
        print(new_line)
    return render_template("update.html", line=new_line, no=(no+1))


@app.route("/update/<int:no>", methods=["POST"])
def update_todo(no):
    todos = func.read_todos_from_db()
    no = int(no) - 1

    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != todos[no]:
                f.write(i)
            else:
                new_i = request.form.get("title")
                f.write(new_i)
                f.write("\n")
                s = '"'+new_i+'"'
                print("Updated todo: {} {} to {}".format((no+1), i, s))
        f.truncate()

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
