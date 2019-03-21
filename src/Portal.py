import os
import src.config as CFG
from src.Matrix import Matrix
import pickle
from util.Utils import load_matrix

class Portal():
    def __init__(self):

        # load Matrix
        if os.path.isfile(CFG.default_matrix):
            self.matrix = load_matrix()
        else:
            self.matrix = Matrix()

        # load commands
        self.commands = self.load_commands()

    def save_matrix(self):
        with open(CFG.default_matrix, 'wb') as handle:
            pickle.dump(self.matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_commands(self):
        commands = {
            'create_person': self.matrix.create_person,
            'create_baby': self.matrix.create_baby,
            'remove_person': self.matrix.delete_person,
            'list_people': self.matrix.list_people,
            'create_food': self.matrix.create_food,
            'remove_item': self.matrix.delete_thing,
            'assign': self.matrix.assign_item,
            'list_item': self.matrix.list_thing,
            'run_turns': self.matrix.run_n_turn,
            'focus': self.matrix.show_person
        }
        return commands