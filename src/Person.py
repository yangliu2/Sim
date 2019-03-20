from src.Entity import Entity
import random
import src.config as CFG

class Person(Entity):

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        name = f'{self.first_name}_{self.last_name}'
        super().__init__(name)

        self.age = 0
        self.gender = random.choice(['MALE', 'FEMALE'])
        self.dad = None
        self.mom = None
        self.health = 10
        self.energy = 10
        self.alive = True
        self.aptite = 0 # 1-10, hungry to full
        self.possession = []

    def eat_food(self, food):
        print(f'eating {food}')
        if self.energy > 10:
            print(f'Full.')
        else:
            need = 10 - self.energy
            if food.hunger_value < need:
                self.energy += food.hunger_value
                food.value = 0
                print(f'{self.name} ate some {food.name}. But they are still hungrey.')
            else:
                self.energy += need
                food.hunger_value -= need
                print(f'{self.name} ate some {food.name}. And they are no longer hungrey.')

    def get_food_list(self):
        food_list = []
        for item in self.possession:
            if item.type == 'FOOD':
                food_list.append(item)
        return food_list

    def eat(self):
        food_list = self.get_food_list()
        print(food_list)
        if food_list:
            food = random.choice(food_list)
            self.eat_food(food)
    
    def __str__(self):
        possession = [x.name for x in self.possession]
        status = f"First name: {self.first_name} \
                        Last Name: {self.last_name} \
                        Gender: {self.gender} \
                        Health: {self.health} \
                        Energy: {self.energy} \
                        Possessions: {possession}"
        return status

    def __repr__(self):
        possession = [x.name for x in self.possession]
        status = f"First name: {self.first_name} \
                        Last Name: {self.last_name} \
                        Gender: {self.gender} \
                        Health: {self.health} \
                        Energy: {self.energy} \
                        Possessions: {possession}"
        return status

    def calc_expense(self):
        if self.energy <= 0:
            self.health -= 1
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
        

def main():
    pass

if __name__ == "__main__":
    main()