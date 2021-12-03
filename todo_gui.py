import tkinter as tk

# global list for storing all the todo
todos_list = []

# global variable for counting the todo
counter = 1


# Function for checking input error
# when empty input is given
def inputError():

    if enterTodoField.get() == "":
        tk.messagebox.showerror("Input Error")
        return 0
    return 1


# Function for clearing the contents
# of todo number field
def clear_todoNumberField():
    todoNumberField.delete(0.0, tk.END)


# Function for clearing the contents
# from the todo entry field to the text area
def clear_todoField():
    enterTodoField.delete(0, tk.END)


# Function for inserting the contents
# from the todo entry field to the text area
def add_todo():
    global counter

    # Check for error
    value = inputError()

    # if error occure then return
    if value == 0:
        return

    # get and store TODO
    content = enterTodoField.get() + "\n"
    todos_list.append(content)

    # Insert content of todo entry field to the text area
    # Add todo one by one in below one by one
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ]" + content)
    counter += 1

    clear_todoField()


def delete_todo():

    global counter

    if len(todos_list) == 0:
        tk.messagebox.showerror("No todos")
        return

    # Get the todo number, wich is required to delete
    number = todoNumberField.get(1.0, tk.END)

    # checking for input error when
    # empty input in todo number field
    if number == "\n":
        tk.messagebox.showerror("input error")
        return
    else:
        todo_no = int(number)

        # function calling for deleting the
        # content of todo number field
        clear_todoNumberField()

        todos_list.pop(todo_no - 1)

        counter -= 1

        # whole content of text area widget is deleted
        TextArea.delete(1.0, tk.END)

        # rewriting the todo after deleting one todo at a time
        for i in range(len(todos_list)):
            str1 = 'end -1 chars', "[ " + str(i + 1) + " ]  " + todos_list[i]
            TextArea.insert(str1)


def update_todo(no):
    pass


def done_todo(no):
    pass


# Driver code
if __name__ == "__main__":

    # create a GUI window
    gui = tk.Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("TODO App")

    # set the configuration of GUI window
    gui.geometry("300x350")

    # create a label : Enter Your Todo
    enterTodo = tk.Label(gui, text="Enter Your Todo", bg="light green")
    enterTodo.grid(row=0, column=2)

    # create a text entry box
    # for typing the todo
    enterTodoField = tk.Entry(gui)
    enterTodoField.grid(row=1, column=2, ipadx=58)

    # create a Submit Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed
    Submit = tk.Button(
        gui, text="Submit", fg="Black", bg="Red", command=add_todo
    )
    Submit.grid(row=2, column=2, padx=10, pady=5, sticky="e")

    # create a text area for the root
    TextArea = tk.Text(gui, height=6, width=25, font="lucida 13")
    TextArea.grid(row=3, column=2, padx=10, sticky=tk.W)

    # create a label : Delete Todo Number
    todoNumber = tk.Label(
        gui, text="Enter Todo Number", bg="blue", height=1, width=22
    )
    todoNumber.grid(row=4, column=2, padx=46, pady=5, sticky="e")

    todoNumberField = tk.Text(gui, height=1, width=2, font="lucida 13")
    todoNumberField.grid(row=4, column=2, padx=10, pady=5, sticky="e")

    # create a Delete Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed .
    done = tk.Button(
        gui, text="Done", fg="Black", bg="White", command=done_todo
    )
    update = tk.Button(
        gui, text="Update", fg="Black", bg="Green", command=update_todo
    )
    delete = tk.Button(
        gui, text="Delete", fg="Black", bg="Red", command=delete_todo
    )
    done.grid(row=5, column=2, padx=75, pady=5, sticky="w")
    update.grid(row=5, column=2, padx=85, pady=5, sticky="e")
    delete.grid(row=5, column=2, padx=10, pady=5, sticky="e")

    # create a Exit Button and place into the root window
    Exit = tk.Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
    Exit.grid(row=7, column=2, padx=10, pady=5, sticky="e")

    # start the GUI
    gui.mainloop()
