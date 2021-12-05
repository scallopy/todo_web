import os
import tkinter as tk
import main as func
from tkinter import messagebox, ttk

import errno


# Function for checking input error
# when empty input is given
def inputError():
    if enterTodoField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1


def inputNumberErrors(no, todos):
    if no == "\n":
        messagebox.showerror("Type todo number!")
        clear_todoNumberField()
        return

    no = int(no)
    if no not in range(1, (len(todos)+1)):
        messagebox.showinfo("No todo!")
        clear_todoNumberField()
        return


def refresh():
    try:
        gui.destroy()
        os.popen("python3.8 todo_gui.py")
    except IOError as e:
        if e.errno == errno.EPIPE:
            messagebox.showerror("IOError!")
            return


# Function for clearing the contents
# of todo number field
def clear_todoNumberField():
    todoNumberField.delete(0.0, tk.END)


def update_fields():
    TextArea.configure(state="normal")
    TextArea.delete('1.0', tk.END)
    content = func.lsTodo()
    for item in content:
        TextArea.insert(tk.END, item[0])
    TextArea.configure(state='disabled')
    enterTodoField.delete(0, tk.END)


def remove_update_fields():
    updateTodoField.delete(0, tk.END)
    updateTodoField.grid_remove()
    updateTodo.grid_remove()
    cancel.grid_remove()


def addUpdateRow():
    no = todoNumberField.get(1.0, tk.END)
    todos = func.read_todos_from_db()

    try:
        no = int(no) - 1
        if no not in range(0, (len(todos))):
            messagebox.showinfo("No todo!")
            clear_todoNumberField()
            return

        else:
            updateTodoField.grid(row=7, column=2, ipadx=58)
            updateTodoField.insert(tk.END, todos[no])
            updateTodoField.focus()
            updateTodo.grid(row=8, column=2, padx=10, pady=5, sticky="e")
            cancel.grid(row=8, column=2, padx=105, pady=5, sticky="w")

    except Exception:
        inputNumberErrors(no, todos)


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
    no = todoNumberField.get(1.0, tk.END)
    todos = func.read_todos_from_db()
    try:
        func.deleteTodo(no)

        # clear content of todo number field
        clear_todoNumberField()
        update_fields()
    except Exception:
        inputNumberErrors(no, todos)


def update_todo():
    no = todoNumberField.get(1.0, tk.END)
    todos = func.read_todos_from_db()

    no = int(no) - 1
    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i != todos[no]:
                f.write(i)
            else:
                new_i = updateTodoField.get()
                f.write(new_i)
                f.write("\n")
                s = '"'+new_i+'"'
                print("Updated todo: {} {} to {}".format((no+1), i, s))
        f.truncate()

    remove_update_fields()
    clear_todoNumberField()
    update_fields()


def complete_todo():
    no = todoNumberField.get(1.0, tk.END)
    todos = func.read_todos_from_db()

    try:
        func.completeTodo(no)
        clear_todoNumberField()

        # upate TextArea and Report
        update_fields()
        report_todo()
        messagebox.showinfo("showinfo", "Market todo #{} as done.".format(no))
    except Exception:
        inputNumberErrors(no, todos)


def report_todo():
    Report.configure(state='normal')
    cont = func.reportCompletedTodo()
    for key, value in cont.items():
        if not isinstance(value, list):
            Report.insert(tk.END, (value + "\n\n"))
        else:
            for el in value:
                Report.insert(tk.END, (el + "\n"))
    Report.configure(state='disabled')


# Driver code
if __name__ == "__main__":

    # create and set GUI window:
    gui = tk.Tk()
    gui.configure(background="light green")
    gui.title("TODO App")
    gui.geometry("300x500")

    # create and set tabs:
    tabControl = ttk.Notebook(gui)
    s = ttk.Style()
    s.configure('TFrame', background="light green")
    s.configure('Frame1.TFrame', background='light blue')

    tab1 = ttk.Frame(tabControl, style='TFrame')
    tab2 = ttk.Frame(tabControl, style='Frame1.TFrame')

    tabControl.add(tab1, text="Add TODO")
    tabControl.add(tab2, text="Completed TODOs")
    tabControl.pack(expand=1, fill="both")

    # Drawing a tab1:

    # create and display add todo box
    enterTodo = tk.Label(tab1, text="Enter Your Todo:", bg="light green")
    enterTodo.grid(row=0, column=2, padx=10, pady=(20, 5), sticky="w")

    enterTodoField = tk.Entry(tab1)
    enterTodoField.focus()
    enterTodoField.grid(row=1, column=2, ipadx=58)

    # Submit button to add a todo
    Submit = tk.Button(
        tab1, text="Submit", fg="Black", bg="Red", command=add_todo
    )
    tab1.bind('<Return>', lambda event: add_todo())
    Submit.grid(row=2, column=2, padx=10, pady=5, sticky="e")

    # Create an area to display added todos
    TextArea = tk.Text(tab1, height=8, width=25, font="lucida 13")
    TextArea.grid(row=3, column=2, padx=10, sticky=tk.W)

    content1 = func.lsTodo()
    for item in content1:
        TextArea.insert(tk.END, item[0])
    TextArea.configure(state='disabled')

    # Creat Todo Number field
    todoNumber = tk.Label(
        tab1, text="Enter Todo Number - >", height=1, width=22
    )
    todoNumber.grid(row=5, column=2, padx=46, pady=5, sticky="e")

    todoNumberField = tk.Text(tab1, height=1, width=2, font="lucida 13")
    todoNumberField.grid(row=5, column=2, padx=10, pady=5, sticky="e")

    # Create Done, Update, and Delete buttons:
    done = tk.Button(
        tab1, text="Done", fg="Black", bg="White", command=complete_todo
    )
    done.grid(row=6, column=2, padx=75, pady=5, sticky="w")

    updateButton = tk.Button(
        tab1, text="Update", fg="Black", bg="Green", command=addUpdateRow
    )
    updateButton.grid(row=6, column=2, padx=85, pady=5, sticky="e")

    delete = tk.Button(
        tab1, text="Delete", fg="Black", bg="Red", command=delete_todo
    )
    delete.grid(row=6, column=2, padx=10, pady=5, sticky="e")

    # Display fields to update a todo:
    updateTodoField = tk.Entry(tab1)
    updateTodo = tk.Button(
        tab1,
        text="Update Todo", fg="Black", bg="Green", command=update_todo
    )
    cancel = tk.Button(
        tab1,
        text="Cancel", fg="Black", command=remove_update_fields
    )

    # Create refresh button to update code changes:
    Refresh = tk.Button(tab1, text="Refresh", command=refresh)
    Refresh.grid(row=11, column=2, padx=10, pady=10, sticky="se")

    # Drawing tab2 for completed todos
    completed = tk.Label(tab2, text="Completed todos")
    completed.grid(row=1, column=2)

    Report = tk.Text(tab2, height=20, width=34, font="lucida 10")
    Report.grid(row=2, column=2, padx=10, sticky=tk.W)
    report_todo()

    # start the GUI
    gui.mainloop()
