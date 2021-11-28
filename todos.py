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


# Function to complete a todo
def done_todo(no):
    todos = read_todos_from_db()
    no = int(no) - 1
    f = open('done.txt', 'a')
    st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + todos[no]

    f.write(st)
    f.close()
    print("Market todo #{} as done.".format(no))

    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != todos[no]:
                f.write(i)
        f.truncate()


def done(no):
    try:
        done_todo(no)

    except Exception:
        print("Error: todo #{} does not exist.".format(no))


# Function to show report/statistics of todo list
def report():
    todos = read_todos_from_db()
    try:

        nf = open('done.txt', 'r')
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

    except Exception:
        print(
            '{} Pending : {} Compleated : {}'
            .format(str(datetime.datetime.today()).split()[0],
                    len(todos), len(don))
        )


# delete
def deL(no):
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

        print("Error: todo #{} does not exist. Nothing deleted.".format(no))


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
    # try:
        don = {}
        args = sys.argv

        if (args[1] == 'del'):
            args[1] = 'deL'

        if (args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.write("Error: Missing todo string. Nothing added!")
        elif (args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.write("Error: Missing NUMBER for done todo.")
        elif (args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.write("Error: Missing NUMBER for deleting todo.")
        else:
            globals()[args[1]](*args[2:])

    # except Exception:
    #     # TODO: Reuse the 'help' function.
    #     s = """Usage : -
    #     $ ./todo add "todo item"  # Add a new todo
    #     $ ./todo ls               # Show remaining todos
    #     $ ./todo del NUMBER       # Delete a todo
    #     $ ./todo done NUMBER      # Complete a todo
    #     $ ./todo help             # Show usage
    #     $ ./todo report           # Statistics"""
    #     sys.stdout.write(s)
