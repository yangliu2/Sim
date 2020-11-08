import unittest
from panzoto.person import Person
from panzoto.enums import PersonStatus, ThingStatus
from panzoto.food import Food


class TestPerson(unittest.TestCase):
    def setUp(self):
        # person 
        self.first_name = "Yang"
        self.last_name = "Liu"
        self.person = Person(self.first_name, self.last_name)

        # food
        self.food_value = 5
        self.food_name = "Apple"
        self.item_type = ThingStatus.FOOD.value
        self.food = Food(name=self.food_name,
                         value=self.food_value)

        # possession assign
        self.person.possession.append(self.food)

    def tearDown(self):
        pass

    def test_eat_food(self):
        self.person.energy = 5
        self.person.eat_food(self.food)
        
        actual = self.person.energy
        expected = self.person.energy + self.food.food_value
        self.assertEqual(
            actual,
            expected,
            msg="After eat food, the person's energy did not increase correctly",
        )

    def test_get_food_list(self):
        # remember the list of food is a list of objects, not str
        
        actual = self.person.get_food_list()
        expected = [self.food]
        self.assertEqual(
            actual,
            expected,
            msg="A list of food need to match the food the person have",
        )

    def test_get_food_list_no_food(self):

        # check when if no food is the path
        self.person.possession = []
        self.person.energy = 5
        self.person.eat()

        actual = self.person.energy
        expected = 5
        self.assertEqual(
            actual,
            expected,
            msg="When there is no food, should not change energy.",
        )

    def test_calc_expense_enough_energy1(self):

        self.person.energy = 1
        self.person.health = 9
        self.person.calc_expense()

        actual = self.person.health
        expected = 10
        self.assertEqual(
            actual,
            expected,
            msg="Health should increase if there is still energy.",
        )

    def test_calc_expense_enough_energy2(self):

        self.person.energy = 1
        self.person.health = 10
        self.person.calc_expense()

        actual = self.person.health
        expected = 10
        self.assertEqual(
            actual,
            expected,
            msg="Health should stay at 10 even with enough energy.",
        )

    def test_calc_expense_not_enough_energy(self):

        self.person.energy = 0
        self.person.health = 9
        self.person.calc_expense()

        actual = self.person.health
        expected = 8
        self.assertEqual(
            actual,
            expected,
            msg="Health should decrease if there is no energy.",
        )

    def test_check_status(self):

        self.person.health = 0
        self.person.check_status()

        actual = self.person.alive
        expected = False
        self.assertEqual(
            actual,
            expected,
            msg="Person should not be alive if health falls below 0.",
        )
