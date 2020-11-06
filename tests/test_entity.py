import unittest
from panzoto.entity import Entity


class TestEntity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_eq_false(self):
        name = "apple"
        actual = Entity(name).uid == Entity(name).uid
        expected = False
        self.assertEqual(
            actual, 
            expected, 
            msg="Entites with the same name should not be equal."
        )


if __name__ == "__main__":
    unittest.main()
