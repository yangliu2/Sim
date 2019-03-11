from src.Person import Person
from src.Food import Food
from util.Utils import pline

class Matrix():

    def __init__(self):
        self.people_dict = {}
        self.food_list = {}

    def create_person(self, first_name, last_name):
        person = Person(first_name, last_name)
        print(f'{person.name} created.')
        self.people_dict[person.name] = person

    def list_people(self):
        if not self.people_dict:
            print(f'No people exist.')

        for person in self.people_dict:
            print(f'{person}')

    def show_person(self, name):
        if name in self.people_dict:
            print(f'{self.people_dict[name]}')
        else:
            print(f'Cannot find the person you are searching.')

    def create_food(self, name, value):
        food = Food(name, value)
        print(f'{food.name} created.')
        self.food_list[food.name] = food

    def list_food(self):
        if not self.food_list:
            print(f'No food exist.')

        for food in self.food_list:
            print(f'{food}')

    def run_iter(self, num):
        for i in range(num):
            print(f'Iter: {i}')
