import unittest
from panzoto.matrix import Matrix
from panzoto.food import Food
from panzoto.enums import ThingStatus


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_value = 10
        self.item_value = 5
        self.food_name = "Apple"
        self.item_type = ThingStatus.FOOD.value
        self.food = Food(name=self.food_name,
                         value=self.item_value)

    def tearDown(self):
        pass

    def test_check_status(self):
        # checking if food worth will be set to false if food_value is none
        self.food.food_value = 0
        self.food.check_status()

        actual = self.food.food_worth
        expected = False
        self.assertEqual(
            actual, expected,
            msg=f"Food value of {self.food_value} "
            "should make the food_worth to False.")
