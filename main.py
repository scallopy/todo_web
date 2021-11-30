import datetime


def addTodo(todo_item):
    with open('todo.txt', 'a') as f:
        f.write(todo_item)
        f.write("\n")
    print("Added todo: \"{}\"".format(todo_item))


def ls():
    todos = read_todos_from_db()
    idx = len(todos)

    for todo in reversed(todos):
        print("[{}] {}".format(idx, todo))
        idx -= 1


def complete_todo(no):
    try:
        todos = read_todos_from_db()
        no = int(no) - 1
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + todos[no]

        f.write(st)
        f.close()
        print("Market todo #{} as done.".format(no+1))

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != todos[no]:
                    f.write(i)
            f.truncate()
    except Exception:
        print("Error: todo #{} does not exist. Nothing comleted.".format(no+1))


def reportCompletedTodo():
    completed = []
    todos = read_todos_from_db()
    don = {}
    cont = ""
    with open('done.txt', 'r') as nf:
        c = 0
        for line in nf:
            c = c + 1
            don.update({c: line})

        cont += (
            '{} Pending : {} Compleated : {}'
            .format(str(datetime.datetime.today()).split()[0],
                    len(todos), len(don))
        )
    for value in don.values():
        completed.append(value)

    content = {
        "cont": cont,
        "completed": completed
    }
    return content


def delete_todo(no):
    try:
        no = int(no) - 1
        todos = read_todos_from_db()

        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i != todos[no]:
                    f.write(i)
            f.truncate()
        print("Deleted todo #{}".format(no + 1))
    except Exception:
        print("Error: todo #{} does not exist. Nothing deleted.".format(no+1))


def read_todos_from_db():
    todos = []
    try:
        with open('todo.txt', 'r') as f:
            for line in f:
                line.strip('\n')
                todos.append(line)
        return todos
    except Exception:
        print("There are no pending todos!")
