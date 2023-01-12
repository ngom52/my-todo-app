try:
    def get_todos(filepath='../web_app1/todos.txt'):
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
except FileNotFoundError:
    def get_todos(filepath='..\web_app1\todos.txt'):
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local

try:
    def write_todos(todos_arg, filepath='../web_app1/todos.txt'):
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)
except FileNotFoundError:
    def write_todos(todos_arg, filepath='..\web_app1\todos.txt'):
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)
