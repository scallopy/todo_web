import sys
import datetime
import main as func

def help():
    help_message = """Usage : -
        $ ./todo add "todo item"       # Add a new todo
        $ ./todo ls                    # Show remaining todos
        $ ./todo del NUMBER            # Delete a todo
        $ ./todo done NUMBER           # Compleate a todo
        $ ./todo help                  # Show usage
        $ ./todo report                # Statistics
        $ ./todo update NUM "new item" # Update a todo
        """
    print(help_message)


def add(todo_item):
    func.addTodo(todo_item)


def ls_todo():
    content = func.lsTodo()
    for item in content:
        print(item[0])

def complete_todo(no):
    try:
        func.completeTodo(no)
    except Exception:
        print("Error: todo #{} does not exist. Nothing comleted.".format(no))


def report_completed_todo():
    try:
        content = func.reportCompletedTodo()
        print(content["cont"])
    except Exception:
        print("There are not completed todos!")


def update_todo(no, new_item):
    try:
        todos = func.read_todos_from_db()
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
                    s = '"'+new_item+'"'
                    print("Updated todo: {} {} to {}".format((no+1), i, s))
            f.truncate()
    except Exception:
        print("Error: todo #{} does not exist. Nothing updated.".format(no+1))


def delete_todo(no):
    try:
        func.deleteTodo(no)
        print("Deleted todo #{}".format(no + 1))
    except Exception:
        print("Error: todo #{} does not exist. Nothing deleted.".format(no+1))




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
            if (args[1] == 'update'):
                args[1] = 'update_todo'
            if (args[1] == 'ls'):
                args[1] = 'ls_todo'
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
