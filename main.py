import datetime


def addTodo(todo_item):
    with open('todo.txt', 'a') as f:
        f.write(todo_item)
        f.write("\n")


def lsTodo():
    todos = read_todos_from_db()
    inx = len(todos)
    content = []
    for todo in reversed(todos):
        cont = [("[{}] {}\n".format(inx, todo)), inx]
        inx -= 1
        content.append(cont)
    return content


def completeTodo(no):
    todos = read_todos_from_db()
    no = int(no) - 1
    f = open('done.txt', 'a')
    st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + todos[no]

    f.write(st)
    f.close()

    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != todos[no]:
                f.write(i)
        f.truncate()


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


def updateTodo(no, new_item):
    todos = read_todos_from_db()
    no = int(no) - 1
    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != todos[no]:
                f.write(i)
            else:
                f.write(new_item)
                f.write("\n")
        f.truncate()




def deleteTodo(no):
    no = int(no) - 1
    todos = read_todos_from_db()
    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != todos[no]:
                f.write(i)
        f.truncate()


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
