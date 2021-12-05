# Todo Apps

## Getting Started

1. Install Python3.8

    ```
    $ python --version
    Python 3.7.3
    $ which python3.8
    /usr/local/bin/python3.8
    $ alias python="/usr/local/bin/python3.8"
    $ python --version
    Python 3.8.4
    ```

2. Clone the repo: `$ git@github.com:scallopy/todo_web.git`

3. Create virtualenv: `$ virtualenv -p python3.8 env`

4. Activate virtualenv: `source env/bin/activate`

5. Install the requirements: `(env) ...$ python3.8 -m pip install -U -r requirements.txt`

## To run `Web` version

Run the server: `python todo_web.py`

## Working with `CLI` vertion:

1. Give permition to the todo.sh: `$ chmod +x todo.sh`

2. How to use app: `$ ./todo help`

3. If you haven't linked todo.sh:

- for Linux: `$ ln -s todo.sh todo`

- for Windows:

**todo.bat** file:

```
@echo off
python3 todo.py %1 %2
```

**Create a symbolic link to the executable file:**

`mklink todo todo.bat`

## To run `GUI` version:

`python3.8 todo_gui.py`

**Note: The `Refresh` button doesn't work very well at this point - IOError
sometimes appears, but I use it when I make changes.**
