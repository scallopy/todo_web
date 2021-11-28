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


# Function to print the todo list items
def ls():

    try:

        nec()
        k = len(d)

        for i in d:
            sys.stdout.write("[{}] {}".format(k, d[k]))
            sys.stdout.write("\n")
            k = k - 1

    except Exception as e:
        raise e


# Function to complete a todo
def done_todo(no):
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


def done(no):
    try:
        done_todo(no)

    except Exception:
        print("Error: todo #{} does not exist.".format(no))


# Function to show report/statistics of todo list
def report():
    nec()
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
                    len(d), len(don))
        )

    except Exception:
        print(
            '{} Pending : {} Compleated : {}'
            .format(str(datetime.datetime.today()).split()[0],
                    len(d), len(don))
        )


# delete
def deL(no):
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


# Main function and utility function
def nec():

    # Utility function uset in done and report function
    try:
        f = open('todo.txt', 'r')
        c = 0
        d.clear()
        for line in f:
            line.strip('\n')
            c = c + 1
            d[c] = line
        f.close()

    except Exception:
        sys.stdout.write("There are no pending todos!")


# Main program
if __name__ == '__main__':
    try:
        d = {}
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

    except Exception:

        s = """Usage : -
        $ ./todo add "todo item"  # Add a new todo
        $ ./todo ls               # Show remaining todos
        $ ./todo del NUMBER       # Delete a todo
        $ ./todo done NUMBER      # Complete a todo
        $ ./todo help             # Show usage
        $ ./todo report           # Statistics"""
        sys.stdout.write(s)
