from pathlib import Path
import pickle
from rich.table import Table
from rich import box
from rich.console import Console
from typing import Callable, Dict
import panzoto.config as CFG
from panzoto.matrix import Matrix
from panzoto.utils import load_matrix, log_output, timer


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
    def save_matrix(self,
                    save_path: str = CFG.default_matrix) -> None:
        """Save the world data in a pickle file

        Args:
            save_path (str, optional): save matrix file path. 
            Defaults to CFG.default_matrix.
        """
        file_path = Path(save_path)
        if not file_path.parent.exists():
            Path(file_path.parent).mkdir(parents=True, exist_ok=True)

        with open(file_path, 'wb') as handle:
            pickle.dump(self.matrix,
                        handle,
                        protocol=pickle.HIGHEST_PROTOCOL)

    def load_commands(self) -> Dict[str, Callable]:
        """Lists of commands 

        Returns:
            Dict: dict of commands, {command: function to call}
        """
        commands = {
            # create_person <first name> <last name>
            'create_person': self.matrix.create_person,
            'create_people': self.matrix.create_people,
            'create_child': self.matrix.create_child,
            'remove_person': self.matrix.delete_person,
            'list_people': self.matrix.list_people,
            'create_food': self.matrix.create_food,
            'remove_item': self.matrix.delete_thing,
            'assign': self.matrix.assign_item,
            'list_items': self.matrix.list_things,
            'run_turns': self.matrix.run_n_turn,
            'focus': self.matrix.focus,
            'show_stats': self.matrix.show_stats,
            'show_records': self.matrix.show_records,
            'graph_stats': self.matrix.graph_stats,
            'help': self.show_commands
        }
        return commands

    def show_commands(self) -> str:
        """Display a list of commands

        Returns:
            str: output string
        """
        output = ""
        commands = self.load_commands()
        table = Table(title="Matrix Commands", box=box.ROUNDED)
        table.add_column("Commands", 
                          justify="left", 
                          style="cyan")

        for key in commands:
             table.add_row(key)

        console = Console()
        console.print(table)

        return output
