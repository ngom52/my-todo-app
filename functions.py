def get_todos(filepath='C:/Users/10091992/Documents/PycharmProjects/pythonProject/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='C:/Users/10091992/Documents/PycharmProjects/pythonProject/todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
