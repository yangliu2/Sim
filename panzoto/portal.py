from pathlib import Path
import pickle
from typing import Dict
import panzoto.config as CFG
from panzoto.matrix import Matrix
from panzoto.utils import load_matrix, timer


class Portal():
    def __init__(self):

        # load Matrix
        if Path(CFG.default_matrix).exists():
            self.matrix = load_matrix()
        else:
            self.matrix = Matrix()

        # load commands
        self.commands = self.load_commands()

    @timer
    def save_matrix(self) -> None:
        """Save the world data in a pickle file
        """
        file_path = Path(CFG.default_matrix)
        if not file_path.parent.exists():
            Path(file_path.parent).mkdir(parents=True, exist_ok=True)

        with open(file_path, 'wb') as handle:
            pickle.dump(self.matrix,
                        handle,
                        protocol=pickle.HIGHEST_PROTOCOL)

    def load_commands(self) -> Dict:
        """Lists of commands 

        Returns:
            Dict: dict of commands, {command: function to call}
        """
        commands = {
            # create_person <first name> <last name>
            'create_person': self.matrix.create_person,
            'create_child': self.matrix.create_child,
            'remove_person': self.matrix.delete_person,
            'list_people': self.matrix.list_people,
            'create_food': self.matrix.create_food,
            'remove_item': self.matrix.delete_thing,
            'assign': self.matrix.assign_item,
            'list_items': self.matrix.list_things,
            'run_turns': self.matrix.run_n_turn,
            'focus': self.matrix.focus,
            'help': self.show_commands
        }
        return commands

    def show_commands(self) -> None:
        """Display a list of commands that's currently avaiable
        """
        commands = self.load_commands()
        for key in commands:
            print(key)
