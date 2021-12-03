import tkinter as tk
import main as func
from tkinter import messagebox, ttk

# global list for storing all the todo
todos_list = []

# global variable for counting the todo
counter = 1


# Function for checking input error
# when empty input is given
def inputError():

    if enterTodoField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1


# Function for clearing the contents
# of todo number field
def clear_todoNumberField():
    todoNumberField.delete(0.0, tk.END)


def update_fields():
    TextArea.delete('1.0', tk.END)
    content = func.lsTodo()
    for item in content:
        TextArea.insert(tk.END, item[0])
    TextArea.configure(state='disabled')
    enterTodoField.delete(0, tk.END)


# Function for inserting the contents
# from the todo entry field to the text area
def add_todo():

    # Check for error
    value = inputError()

    # if error occure then return
    if value == 0:
        return

    # get and store TODO
    todo_item = enterTodoField.get()
    func.addTodo(todo_item)

    # upate TextArea
    TextArea.configure(state="normal")
    update_fields()


def delete_todo():

    # Get the todo number, wich is required to delete
    no = todoNumberField.get(1.0, tk.END)

    # checking for input error when
    # empty input in todo number field
    if no == "\n":
        messagebox.showerror("input error")
        clear_todoNumberField()
        return
    else:
        func.deleteTodo(no)

        # clear content of todo number field
        clear_todoNumberField()

        # upate TextArea
        TextArea.configure(state="normal")
        update_fields()


def update_todo(no):
    pass


def complete_todo():
    # Get the todo number, wich is required to delete
    no = todoNumberField.get(1.0, tk.END)

    # checking for input error when
    # empty input in todo number field
    if no == "\n":
        messagebox.showerror("input error")
        clear_todoNumberField()
        return
    else:
        func.completeTodo(no)

        # clear content of todo number field
        clear_todoNumberField()

        # upate TextArea
        TextArea.configure(state="normal")
        update_fields()
        report_todo()
        messagebox.showinfo("showinfo", "Market todo #{} as done.".format(no))


def report_todo():
    Report.configure(state='normal')
    cont = func.reportCompletedTodo()
    for key, value in cont.items():
        if not isinstance(value, list):
            print(value)
            Report.insert(tk.END, (value + "\n\n"))
        else:
            for el in value:
                print(el)
                Report.insert(tk.END, (el + "\n"))
    Report.configure(state='disabled')


# Driver code
if __name__ == "__main__":

    # create a GUI window
    gui = tk.Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("TODO App")

    # set the configuration of GUI window
    gui.geometry("300x420")

    tabControl = ttk.Notebook(gui)
    s = ttk.Style()
    s.configure('TFrame', background="light green")
    s.configure('Frame1.TFrame', background='light blue')

    tab1 = ttk.Frame(tabControl, style='TFrame')
    tab2 = ttk.Frame(tabControl, style='Frame1.TFrame')

    tabControl.add(tab1, text="Add TODO")
    tabControl.add(tab2, text="Report")
    tabControl.pack(expand=1, fill="both")

    # create a label : Enter Your Todo
    enterTodo = tk.Label(tab1, text="Enter Your Todo", bg="light green")
    enterTodo.grid(row=0, column=2)

    # create a text entry box
    # for typing the todo
    enterTodoField = tk.Entry(tab1)
    enterTodoField.focus()
    enterTodoField.grid(row=1, column=2, ipadx=58)

    # when user press the button, the command or
    # function affiliated to that button is executed
    Submit = tk.Button(
        tab1, text="Submit", fg="Black", bg="Red", command=add_todo
    )
    tab1.bind('<Return>', lambda event: add_todo())
    Submit.grid(row=2, column=2, padx=10, pady=5, sticky="e")

    # create a text area for the root
    TextArea = tk.Text(tab1, height=8, width=25, font="lucida 13")
    TextArea.grid(row=3, column=2, padx=10, sticky=tk.W)

    # Read Uncompleted Todos
    content1 = func.lsTodo()
    for item in content1:
        TextArea.insert(tk.END, item[0])
    TextArea.configure(state='disabled')

    completed = tk.Label(tab2, text="Completed todos")
    completed.grid(row=1, column=2)

    Report = tk.Text(tab2, height=20, width=34, font="lucida 10")
    Report.grid(row=2, column=2, padx=10, sticky=tk.W)
    report_todo()

    # create a label : Delete Todo Number
    todoNumber = tk.Label(
        tab1, text="Enter Todo Number - >", height=1, width=22
    )
    todoNumber.grid(row=5, column=2, padx=46, pady=5, sticky="e")

    todoNumberField = tk.Text(tab1, height=1, width=2, font="lucida 13")
    todoNumberField.grid(row=5, column=2, padx=10, pady=5, sticky="e")

    # create a Delete Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed .
    done = tk.Button(
        tab1, text="Done", fg="Black", bg="White", command=complete_todo
    )
    update = tk.Button(
        tab1, text="Update", fg="Black", bg="Green", command=update_todo
    )
    delete = tk.Button(
        tab1, text="Delete", fg="Black", bg="Red", command=delete_todo
    )
    done.grid(row=6, column=2, padx=75, pady=5, sticky="w")
    update.grid(row=6, column=2, padx=85, pady=5, sticky="e")
    delete.grid(row=6, column=2, padx=10, pady=5, sticky="e")

    # create a Exit Button and place into the root window
    Exit = tk.Button(tab1, text="Exit", fg="Black", bg="Red", command=exit)
    Exit.grid(row=7, column=2, padx=10, pady=5, sticky="e")

    # start the GUI
    gui.mainloop()
