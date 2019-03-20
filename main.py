import os
import pickle

import src.config as CFG
from src.Matrix import Matrix
from src.Person import Person
from src.Food import Food
from util.Utils import display_logo, ignored


class Portal():
    def __init__(self):

        # load Matrix
        if os.path.isfile(CFG.default_matrix):
            self.load_matrix()
        else:
            self.matrix = Matrix()

        # load commands
        self.commands = self.load_commands()

    def load_matrix(self):
        with open(CFG.default_matrix, 'rb') as handle:
            self.matrix = pickle.load(handle)

    def save_matrix(self):
        with open(CFG.default_matrix, 'wb') as handle:
            pickle.dump(self.matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_commands(self):
        commands = {
            'create_person': self.matrix.create_person,
            'remove_person': self.matrix.delete_person,
            'list_people': self.matrix.list_people,
            'create_food': self.matrix.create_food,
            'remove_item': self.matrix.delete_thing,
            'assign': self.matrix.assign_item,
            'list_item': self.matrix.list_thing,
            'run_n_turn': self.matrix.run_n_turn,
            'focus': self.matrix.show_person
        }
        return commands

def menu(): 
    display_logo()

    response = ""
    while response != 'exit':
        portal = Portal()
        response = input("> ")

        words = response.split(' ')
        command = words[0]
        args = words[1:]
        
        # try:
        if command.lower() in portal.commands:
            portal.commands[command](*args)
        elif command.lower() == 'exit':
            print(f"Later ya'll!")
        else:
            print(f'Cannot recognize command!') 
        # except TypeError as e:
        #     print(f'Command format was wrong!')
        #     print(e)

        # save matrix
        portal.save_matrix()

def main():
    menu()


if __name__ == "__main__":
    main()