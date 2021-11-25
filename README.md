# todo_web

## Python3.8

```
$ $ python --version
Python 3.7.3
$ which python3.8
/usr/local/bin/python3.8
$ alias python="/usr/local/bin/python3.8"
$ python --version
Python 3.8.4
```

## Clone repo:

`$ git@github.com:scallopy/todo_web.git`

## Create virtualenv:

`$ virtualenv -p python3.8 env`

## Activate virtualenv:

`source env/bin/activate`

## Install requirements:

`(env) ...$ python3.8 -m pip install -U -r requirements.txt`

## run server

`python main.py`

# todo_cli

## Give permition to the todo.sh

$ chmod +x todo.sh

## Working with todo CLI app:

$ ./todo help

## If you haven't linked todo.sh:

$ ln -s todo.sh todo

# for windows:
**todo.bat** file:

```

@echo off
python3 todo.py %1 %2
```

**Create a symbolic link to the executable file:**

`mklink todo todo.bat`

