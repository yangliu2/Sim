import unittest
from panzoto.matrix import Matrix
from panzoto.child import Child
from panzoto.enums import Gender


class TestChild(unittest.TestCase):
    def setUp(self):
        self._matrix = Matrix()
        self.first_name = "Yang"
        self.last_name = "Liu"
        self.full_name = self._matrix.get_full_name(
            first_name=self.first_name, last_name=self.last_name
        )

        # make sure there are at least 1 male and 1 female in the matrix
        while True:
            self._matrix.create_person(self.first_name, self.last_name)
            people_dict = self._matrix.people_dict
            females = [people_dict[x] for x in people_dict 
                        if people_dict[x].gender == Gender.FEMALE.value]
            males = [people_dict[x] for x in people_dict 
                if people_dict[x].gender == Gender.MALE.value]
            if len(females) > 0 and len(males) > 0:
                break

        self._matrix.create_child()

    def tearDown(self):
        pass

    def test_born(self):
        person_uid = [*self._matrix.people_dict][-1]
        actual = self._matrix.people_dict[person_uid].full_name
        expected = self.full_name

        self.assertEqual(actual, expected,
                         msg=f"full name is {self.full_name}")