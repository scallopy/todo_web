import sys
from flask import Flask, render_template, request, redirect, url_for
import datetime

from main import read_todos_from_db, addTodo, reportCompletedTodo, lsTodo

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
    addTodo(s)
    return redirect(url_for("home"))


@app.route('/', methods=["GET"])
def home():
    content = lsTodo()
    return render_template('index.html', content=content)


# Function to complete a todo
@app.route("/done/<int:no>", methods=["GET", "POST"])
def done(no):
    try:

        todos = read_todos_from_db()
        no = int(no) - 1
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + todos[no]

        f.write(st)
        f.close()
        print("Market todo #{} as done.".format(no + 1))

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != todos[no]:
                    f.write(i)
            f.truncate()
            return redirect(url_for("report"))

    except Exception:
        print("Error: todo")
        return redirect(url_for("report"))


@app.route("/edit/<int:no>")
def edit(no):
    todos = read_todos_from_db()
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
def update(no):
    todos = read_todos_from_db()
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
    try:
        todos = read_todos_from_db()
        no = int(no) - 1

        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != todos[no]:
                    f.write(i)
            f.truncate()
            print("Deleted todo #{}".format(no+1))

    except Exception:

        print("Error: todo #{} does not exist. Nothing deleted.".format(no+1))
    return redirect(url_for("home"))


# Function to show report/statistics of todo list
@app.route('/report', methods=["GET"])
def report():
    try:
        content = reportCompletedTodo()
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