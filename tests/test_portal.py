import unittest
from panzoto.portal import Portal
from pathlib import Path


class TestPortal(unittest.TestCase):
    def setUp(self):
        self.portal = Portal()
        self.save_path = "tests/matrix.save"
        self.list_of_commands = [
            'create_person', 
            'create_child',
            'remove_person',
            'list_people',
            'create_food',
            'remove_item',
            'assign',
            'list_items',
            'run_turns',
            'focus',
            'show_stats',
            'show_records',
            'graph_stats',
            'help'
        ]

    def tearDown(self):
        # remove file for next round of testing
        if Path(self.save_path).exists():
            Path(self.save_path).unlink()

    def test_eat_food(self):

        # make sure the file save to the right place
        self.portal.save_matrix(self.save_path)

        actual = Path(self.save_path).exists()
        expected = True
        self.assertEqual(
            actual,
            expected,
            msg="Created matrix file path need to exist.",
        )

    def test_load_commands(self):
        commands_dict = self.portal.load_commands()
        actual = list(commands_dict.keys())
        expected = self.list_of_commands
        self.assertEqual(
            actual,
            expected,
            msg="The commands needs to be the same as listed.",
        )

    def test_load_commands(self):
        actual = self.portal.show_commands()
        expected = "\n".join(self.list_of_commands) + "\n"
        self.assertEqual(
            actual,
            expected,
            msg="Listed command have the same string output.",
        )