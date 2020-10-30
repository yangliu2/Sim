from panzoto.entity import Entity
import random
import panzoto.config as CFG
from panzoto.enums import Gender

class Person(Entity):

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.name = f'{self.first_name}_{self.last_name}'
        self.full_name = f'{first_name.capitalize()}_{last_name.capitalize()}'
        super().__init__(self.name)

        self.age = 0
        self.gender = random.choice([Gender.FEMALE.value, Gender.MALE.value])
        self.dad = None
        self.mom = None
        self.health = 10
        self.energy = 10
        self.alive = True
        self.possession = []
        self.status = (
            f"First name: {self.first_name}, "
            f"Last Name: {self.last_name}, "
            f"ID: {self.uid}, "
            f"Gender: {self.gender}, "
            f"Health: {self.health}, "
            f"Energy: {self.energy}, "
            f"Possessions: {self.possession}"
        )

    def eat_food(self, food):

        need = 10 - self.energy
        if food.value < need:
            self.energy += food.value
            food.value = 0
            print(f'{self.name} ate some {food.name}. But they are still hungrey.')
        else:
            self.energy += need
            food.value -= need
            print(f'{self.name} ate some {food.name}. And they are no longer hungrey.')

    def get_food_list(self):
        food_list = []
        for item in self.possession:
            if item.type == 'FOOD':
                food_list.append(item)
        return food_list

    def eat(self):
        food_list = self.get_food_list()
        if food_list:
            food = random.choice(food_list)
            self.eat_food(food)
    
    def __str__(self):
        return self.status

    def __repr__(self):
        return self.status

    def calc_expense(self):
        if self.energy <= 0:
            self.health -= 1
        elif (self.energy > 0) and (self.health < 10):
            self.health += 1
            self.energy -= 1
        else:
            self.energy -= 1

    def calc_need(self):
        if self.energy < CFG.hunger_check:
            self.eat()

    def run_one_turn(self):
        self.calc_need()
        self.calc_expense()
        self.check_status()

    def check_status(self):
        if self.health <= 0:
            self.alive = False
        
        # updating status
        poss = "None"
        if self.possession:
            possession = [x.name for x in self.possession]
            poss = " ".join(possession)

        self.status = (
            f"First name: {self.first_name}, "
            f"Last Name: {self.last_name}, "
            f"Gender: {self.gender}, "
            f"Health: {self.health}, "
            f"Energy: {self.energy}, "
            f"Possessions: {poss}"
        )

def main():
    pass

if __name__ == "__main__":
    main()