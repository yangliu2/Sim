from src.Person import Person
from src.Food import Food

class Matrix():

    def __init__(self):
        self.people_list = []
        self.food_list = []

    def create_person(self, first_name, last_name):
        person = Person(first_name, last_name)
        print(f'{person} created.')
        self.people_list.append(person)

    def list_people(self):
        for index, person in enumerate(self.people_list):
            print(f'{index+1}. {person.first_name} {person.last_name}')

    def create_food(self, name, value):
        food = Food(name, value)
        print(f'{food} created.')
        self.food_list.append(food)

    def list_food(self):
        for index, food in enumerate(self.food_list):
            print(f'{index+1}. {food.name}')

    def run_iter(self, num):
        for i in range(num):
            print(f'Iter: {i}')
