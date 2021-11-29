import sys
import datetime


def help():
    help_message = """Usage : -
        $ ./todo add "todo item" # Add a new todo
        $ ./todo ls              # Show remaining todos
        $ ./todo del NUMBER      # Delete a todo
        $ ./todo done NUMBER     # Compleate a todo
        $ ./todo help            # Show usage
        $ ./todo report          # Statistics
        """
    print(help_message)


def add(todo_item):
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


def report_completed_todo():
    todos = read_todos_from_db()
    don = {}
    with open('done.txt', 'r') as nf:
        c = 1
        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c + 1

        print(
            '{} Pending : {} Compleated : {}'
            .format(str(datetime.datetime.today()).split()[0],
                    len(todos), len(don))
        )


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


# Main program
if __name__ == '__main__':
    args = sys.argv

    if len(args) <= 1:
        help()
    else:
        try:
            if (args[1] == 'del'):
                args[1] = 'delete_todo'
            if (args[1] == 'report'):
                args[1] = 'report_completed_todo'
            if (args[1] == 'done'):
                args[1] = 'complete_todo'
            if (args[1] == 'add' and len(args[2:]) == 0):
                sys.stdout.write("Error: Missing todo string. Nothing added!")
            elif (args[1] == 'done' and len(args[2:]) == 0):
                sys.stdout.write("Error: Missing NUMBER for done todo.")
            elif (args[1] == 'deL' and len(args[2:]) == 0):
                sys.stdout.write("Error: Missing NUMBER for deleting todo.")
            else:
                globals()[args[1]](*args[2:])
        except KeyError:
            help()
