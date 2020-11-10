import unittest
from panzoto.matrix import Matrix
from panzoto.enums import Gender


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.first_name = "Yang"
        self.last_name = "Liu"
        self.matrix = Matrix()
        self.full_name = self.matrix.get_full_name(
            first_name=self.first_name, last_name=self.last_name
        )

        self.matrix.create_person(self.first_name, self.last_name)
        self.food_name = "Apple"
        self.matrix.create_food(self.food_name, 3)

    def tearDown(self):
        pass

    def test_get_full_name(self):
        actual = self.full_name
        expected = "Yang_Liu"
        self.assertEqual(actual, expected,
                         msg="full name is <Firstname>_<Lastname>")

    def test_create_person(self):

        # get a count before and after because there could be duplicate names
        people_dict = self.matrix.people_dict
        names_before = [
            people_dict[x].full_name
            for x in people_dict
            if people_dict[x].full_name == self.full_name
        ]

        self.matrix.create_person(self.first_name, self.last_name)

        people_dict = self.matrix.people_dict
        names_after = [
            people_dict[x].full_name
            for x in people_dict
            if people_dict[x].full_name == self.full_name
        ]

        actual = len(names_after) > len(names_before)
        expected = True
        self.assertEqual(
            actual,
            expected,
            msg="The number of names with 'Yang_Liu' did not increase after "
            "creation of the person.",
        )

    def test_delete_person(self):

        # get the hex of UUID of the first person created in setUp
        people_dict = self.matrix.people_dict
        uid = [*people_dict][0]
        self.matrix.delete_person(uid.hex)

        actual = uid in people_dict
        expected = False
        self.assertEqual(
            actual,
            expected,
            msg="The uid for Yang_Liu need to be deleted from people_dict",
        )

    def test_list_people(self):
        actual = "Yang_Liu\n"
        expected = self.matrix.list_people()
        self.assertEqual(
            actual, expected, msg="Did not generate a list of people.",
        )

    def test_show_person(self):
        # only checked using object itself rather than fixed text because uid
        # change with every new object created in the test
        uid = [*self.matrix.people_dict][0]
        actual = self.matrix.people_dict[uid].status
        expected = self.matrix.show_person(self.first_name, self.last_name)
        self.assertEqual(
            actual, expected, msg="The person's stats did not display correctly",
        )

    def test_assign_item_success(self):
        people_uid = [*self.matrix.people_dict][0]
        thing_uid = [*self.matrix.thing_dict][0]
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=people_uid.hex)
        person_object = self.matrix.people_dict[people_uid]
        thing_object = self.matrix.thing_dict[thing_uid]

        # make sure the person owns the item
        possessions = [x.name for x in person_object.possession]
        actual_1 = thing_object.name in possessions

        # make sure the object's owner is the correct person
        actual_2 = thing_object.owner == person_object.uid
        expected = True

        self.assertEqual(
            actual_1, expected,
            msg=f"{person_object.name} doesn't own {thing_object.name}"
        )
        self.assertEqual(
            actual_2, expected,
            msg=f"{thing_object.name}'s owner is not {person_object.name}"
        )

    def test_assign_item_no_person(self):

        # owner of item doesn't change if no person exist
        people_uid = [*self.matrix.people_dict][0]
        thing_uid = [*self.matrix.thing_dict][0]
        self.matrix.delete_person(people_uid.hex)
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=people_uid.hex)
        thing_object = self.matrix.thing_dict[thing_uid]
        actual = thing_object.owner
        expected = None

        self.assertEqual(
            actual, expected,
            msg=f"Item's owner should not be changed if the person doesn't exist"
        )

    def test_assign_item_no_item(self):

        # person's possession should not have the item if item doesn't exist
        people_uid = [*self.matrix.people_dict][0]
        thing_uid = [*self.matrix.thing_dict][0]
        thing_object = self.matrix.thing_dict[thing_uid]
        thing_name = thing_object.uid.hex
        self.matrix.delete_thing(thing_uid.hex)
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=people_uid.hex)
        people_uid = [*self.matrix.people_dict][0]
        person_object = self.matrix.people_dict[people_uid]
        possessions = [x.name for x in person_object.possession]
        actual = thing_name in possessions
        expected = False

        self.assertEqual(
            actual, expected,
            msg=f"Person should not have the item in possession list"
        )

    def test_create_food(self):

        # get a count before and after because there could be duplicate names
        thing_dict = self.matrix.thing_dict
        name = "Orange"
        names_before = [
            thing_dict[x].name
            for x in thing_dict
            if thing_dict[x].name == name
        ]

        self.matrix.create_food(name, 4)

        thing_dict = self.matrix.thing_dict
        names_after = [
            thing_dict[x].name
            for x in thing_dict
            if thing_dict[x].name == name
        ]

        actual = len(names_after) > len(names_before)
        expected = True
        self.assertEqual(
            actual,
            expected,
            msg="The number of names with 'Orange' did not increase after "
            "creation of the orange.",
        )

    def test_list_things(self):
        actual = self.matrix.list_things()
        expected = "Apple\n"
        self.assertEqual(
            actual, expected, msg="Did not generate a list of people.",
        )

    def test_show_thing(self):
        # compared with the status of the food item
        thing_uid = [*self.matrix.thing_dict][0]
        actual = self.matrix.show_thing(self.food_name)
        expected = f"ID: {thing_uid}, Name: Apple, Owner: None, Food value: 3"
        self.assertEqual(
            actual, expected, msg="Status of food was not displayed correctly",
        )

    def test_remove_item_possession(self):
        # assign an item first, then take away from owner
        thing_uid = [*self.matrix.thing_dict][0]
        thing_object = self.matrix.thing_dict[thing_uid]
        people_uid = [*self.matrix.people_dict][0]
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=people_uid.hex)
        self.matrix.remove_item_possession(thing_uid)
        person_object = self.matrix.people_dict[people_uid]
        possessions = [x.name for x in person_object.possession]

        thing_name = thing_object.uid.hex
        actual = thing_name in possessions
        expected = False
        self.assertEqual(
            actual, expected, msg=f"{person_object.name} still have {thing_name}",
        )

    def test_delete_thing_success(self):
        # compare the length of the thing dict before and after deletion of
        # item because uid of the item changes
        thing_uid = [*self.matrix.thing_dict][0]
        people_uid = [*self.matrix.people_dict][0]
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=people_uid.hex)
        before_deletion = [*self.matrix.thing_dict]
        self.matrix.delete_thing(thing_uid.hex)
        after_deletion = [*self.matrix.thing_dict]
        actual = len(before_deletion) == len(after_deletion)
        expected = False
        self.assertEqual(
            actual, expected,
            msg="Thing dict did not change in size after item deletion",
        )

    def test_delete_thing_check_possession(self):
        # also need to check that item is removed from the owner's possession

        thing_uid = [*self.matrix.thing_dict][0]
        person_uid = [*self.matrix.people_dict][0]
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=person_uid.hex)
        before_deletion = list(self.matrix.people_dict[person_uid].possession)
        self.matrix.delete_thing(thing_uid.hex)
        after_deletion = list(self.matrix.people_dict[person_uid].possession)
        actual = len(before_deletion) == len(after_deletion)
        expected = False
        self.assertEqual(
            actual, expected,
            msg="The item need to be removed from the person's possession.",
        )

    def test_delete_thing_check_person_status(self):
        # also need to check that status is updated for the owner's possession

        thing_uid = [*self.matrix.thing_dict][0]
        person_uid = [*self.matrix.people_dict][0]
        self.matrix.assign_item(thing_uid=thing_uid.hex,
                                person_uid=person_uid.hex)
        before_status = self.matrix.people_dict[person_uid].status
        self.matrix.delete_thing(thing_uid.hex)
        after_status = self.matrix.people_dict[person_uid].status
        actual = after_status
        expected = before_status.rsplit(":",1)[0] + ": []"

        self.assertEqual(
            actual, expected,
            msg="The status needs to be removed from the person's possession.",
        )

    def test_check_people_status(self):
        # change the health of a person below 0 to see if it people status
        # was checked
        count_before = len([*self.matrix.people_dict])
        person_uid = [*self.matrix.people_dict][0]

        self.matrix.people_dict[person_uid].health = -1
        self.matrix.check_people()

        count_after = len([*self.matrix.people_dict])

        actual = count_before == count_after
        expected = False
        self.assertEqual(
            actual, expected,
            msg="1st person will die if health was changed to 0.",
        )

    def test_check_people_output(self):
        # change the health of a person below 0 to see if it people status
        # was checked
        person_uid = [*self.matrix.people_dict][0]
        person_name = self.matrix.people_dict[person_uid].name

        self.matrix.people_dict[person_uid].health = -1
        output = self.matrix.check_people()

        actual = output
        expected = f"{person_name} died."
        self.assertEqual(
            actual, expected,
            msg="Output was wrong when a person died.",
        )

    def test_check_thing_status(self):
        # change the health of a person below 0 to see if it people status
        # was checked
        count_before = len([*self.matrix.thing_dict])
        thing_uid = [*self.matrix.thing_dict][0]

        self.matrix.thing_dict[thing_uid].food_value = 0
        self.matrix.check_things()

        count_after = len([*self.matrix.thing_dict])

        actual = count_before == count_after
        expected = False
        self.assertEqual(
            actual, expected,
            msg="1st thing should be deleted if lost food value.",
        )

    def test_choose_parents(self):
        while True:
            self.matrix.create_person(self.first_name, self.last_name)
            people_dict = self.matrix.people_dict
            females = [people_dict[x] for x in people_dict
                       if people_dict[x].gender == Gender.FEMALE.value]
            males = [people_dict[x] for x in people_dict
                     if people_dict[x].gender == Gender.MALE.value]
            if len(females) > 0 and len(males) > 0:
                break

        mom, dad = self.matrix.choose_parents()
        actual = (mom.gender == Gender.FEMALE.value) and \
            (dad.gender == Gender.MALE.value)
        expected = True
        self.assertEqual(
            actual, expected,
            msg="Make sure the gender of mom and dad are correct. ",
        )


if __name__ == "__main__":
    unittest.main()
