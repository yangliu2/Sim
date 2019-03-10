from src.Matrix import Matrix
from src.Person import Person
from src.Food import Food
from util.Utils import display_logo, ignored

def load_commands(matrix):
    commands = {
        'create_person': matrix.create_person,
        'list_people': matrix.list_people,
        'create_food': matrix.create_food,
        'list_food': matrix.list_food,
        'run_iter': matrix.run_iter
    }

    return commands

def menu(): 
    display_logo()
    response = ""

    matrix = Matrix()
    commands = load_commands(matrix)

    while response != 'exit':
        response = input("> ")

        words = response.split(' ')
        command = words[0]
        args = words[1:]
        
        try:
            if command.lower() in list(commands.keys()):
                commands[command](*args)
            elif command.lower() == 'exit':
                print(f"Later ya'll!")
            else:
                print(f'Cannot recognize command!') 
        except TypeError as e:
            print(f'Command format was wrong!')
            print(e)

def main():
    menu()


if __name__ == "__main__":
    main()