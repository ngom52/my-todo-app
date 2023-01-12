from pathlib import Path

todos_path = Path(__file__).parents[1]/'web_app1/todos.txt'


def get_todos(filepath=todos_path):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#'../web_app1/todos.txt'
def write_todos(todos_arg, filepath=todos_path):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
