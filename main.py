from panzoto.Portal import Portal
from panzoto.Utils import display_logo

def menu(): 
    display_logo()

    response = ""
    while response != 'exit':
        portal = Portal()
        response = input("> ")

        words = response.split(' ')
        command = words[0]
        args = words[1:]
        
        try:
            if command.lower() in portal.commands:
                portal.commands[command](*args)
            elif command.lower() == 'exit':
                print(f"Later ya'll!")
            else:
                print(f'Cannot recognize command!') 
        except TypeError as e:
            print(f'Command format was wrong!')
            print(e)

        # save matrix
        portal.save_matrix()

def main():
    menu()


if __name__ == "__main__":
    main()