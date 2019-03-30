from panzoto.Person import Person
from panzoto.Baby import Baby
from panzoto.Food import Food
from panzoto.Utils import pline

class Matrix():

    def __init__(self):
        self.people_dict = {}
        self.thing_dict = {}

    def create_person(self, first_name, last_name):
        name = f'{first_name.capitalize()}_{last_name.capitalize()}'
        if name in self.people_dict:
            print('Person already exist!')
        else:
            person = Person(first_name, last_name)
            print(f'{person.name} created.')
            self.people_dict[person.name] = person

    def delete_person(self, first_name, last_name):
        name = f'{first_name.capitalize()}_{last_name.capitalize()}'
        if name in self.people_dict:
            del self.people_dict[name]
        else:
            print('That person does not exist!')

    def create_baby(self):
        baby = Baby()
        self.people_dict[baby.name] = baby

    def list_people(self):
        if not self.people_dict:
            print(f'No people exist.')

        for person in self.people_dict:
            print(f'{person}')

    def show_person(self, first_name, last_name):
        name = f'{first_name.capitalize()}_{last_name.capitalize()}'
        if name in self.people_dict:
            print(f'{self.people_dict[name]}')
        else:
            print(f'Cannot find the person you are searching.')

    def assign_item(self, thing, first_name, last_name):
        person = f'{first_name.capitalize()}_{last_name.capitalize()}'
        thing = thing.capitalize()
        if (person in self.people_dict) and (thing in self.thing_dict):
            person_object = self.people_dict[person]
            thing = self.thing_dict[thing.capitalize()]
            thing.owner = person_object
            person_object.possession.append(thing)
            person_object.check_status()
        elif (person in self.people_dict) and (thing not in self.thing_dict):
            print(f"That thing doesn't exist!")
        elif (person not in self.people_dict) and (thing in self.thing_dict):
            print(f"That person doesn't exist!")
        else:
            print(f"Neither that person or the thing exist!")

    def create_food(self, name, value):
        food = Food(name, value)
        print(f'{food.name} created.')
        self.thing_dict[food.name] = food

    def delete_thing(self, thing):
        thing = thing.capitalize()
        if thing in self.thing_dict:
            thing_object = self.thing_dict[thing]
            person = thing_object.owner
            person.possession.remove(thing_object)
            del self.thing_dict[thing_object]
        else:
            print('That thing does not exist!')

    def list_thing(self):
        if not self.thing_dict:
            print(f"Nothing exisit yet.")
            
        for thing in self.thing_dict:
            thing_object = self.thing_dict[thing]
            if thing_object.owner:
                print(f'{thing_object.name}, {thing_object.type}, {thing_object.owner.name}')
            else:
                print(f'{thing_object.name}, {thing_object.type}, {thing_object.owner}')

    def run_n_turn(self, num):
        print(f'Iter: {num} turns.')
        for _ in range(int(num)):
            self.run_one_turn()

    def run_one_turn(self):
        for key in list(self.people_dict):
            person_object = self.people_dict[key]
            
            person_object.run_one_turn()
            # print(f'found {person_object}')

            if not person_object.alive:
                del self.people_dict[key]
                print(f'{person_object.name} died.')

        for key in list(self.thing_dict):
            item_object = self.thing_dict[key]

            if item_object.value <= 0:
                del self.thing_dict[key]
                
                owner = item_object.owner
                owner.possession.remove(item_object)
                owner.check_status()
