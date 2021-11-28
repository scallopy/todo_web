import sys
from flask import Flask, render_template, request, redirect, url_for
import datetime

from todos import add

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
    add(s)
    return redirect(url_for("home"))


@app.route('/', methods=["GET"])
def home():
    nec()
    k = len(d)
    content = []
    for i in d:
        cont = [("[{}] {}\n".format(k, d[k])), k]
        k = k-1
        content.append(cont)
    return render_template('index.html', content=content)


# Function to complete a todo
@app.route("/done/<int:no>", methods=["GET", "POST"])
def done(no):
    try:

        nec()
        no = int(no)
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + d[no]

        f.write(st)
        f.close()
        print("Market todo #{} as done.".format(no))

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != d[no]:
                    f.write(i)
            f.truncate()
            return redirect(url_for("report"))

    except Exception:
        print("Error: todo")
        return redirect(url_for("report"))


@app.route("/edit/<int:no>")
def edit(no):
    no = int(no)
    nec()
    with open("todo.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line == d[no]:
                print(line)
                new_line = line
        print(new_line)
    return render_template("update.html", line=new_line, no=no)


@app.route("/update/<int:no>", methods=["POST"])
def update(no):
    no = int(no)
    nec()

    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != d[no]:
                f.write(i)
            else:
                new_i = request.form.get("title")
                f.write(new_i)
                f.write("\n")
                s = '"'+new_i+'"'
                print("Updated todo: {} {} to {}".format(no, i, s))
        f.truncate()

    return redirect(url_for("home"))


@app.route("/delete/<int:no>", methods=["GET"])
def delete(no):
    try:
        no = int(no)
        nec()

        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != d[no]:
                    f.write(i)
            f.truncate()
            print("Deleted todo #{}".format(no))

    except Exception:

        print("Error: todo #{} does not exist. Nothing deleted.".format(no))
    return redirect(url_for("home"))


# Function to show report/statistics of todo list
@app.route('/report', methods=["GET"])
def report():
    nec()
    try:

        nf = open('done.txt', 'r')
        c = 0
        content = []
        completed = []
        for line in nf:
            c = c + 1
            don.update({c: line})
        cont = (
            '{} Pending : {} Completed : {}'
            .format(
                str(datetime.datetime.today()).split()[0], len(d), len(don))
        )
        content.append(cont)
        for value in don.values():
            completed.append(value)
        return render_template(
            'report.html', content=content, completed=completed)

    except Exception:
        print(
            '{} Pending : {} Compleated : {}'
            .format(
                str(datetime.datetime.today()).split()[0], len(d), len(don))
        )
        return render_template(
            'report.html', content=content, completed=completed)


def nec():

    try:
        f = open("todo.txt", "r")
        lines = f.readlines()
        c = 0
        d.clear()
        for line in lines:
            line.strip('\n')
            c += 1
            d[c] = line
        f.close()

    except Exception:
        print("There are not todos!")


def main(argv):
    reloader = True
    print('Starting with reloader={}'.format(reloader))
    app.run(port=8080, debug=True, use_reloader=reloader)


if __name__ == "__main__":
    d = {}
    don = {}
    main(sys.argv)
