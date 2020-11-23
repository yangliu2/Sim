from panzoto.entity import Entity
import random
from typing import List
import panzoto.config as CFG
from panzoto.enums import Gender, PersonStatus, ThingStatus
from panzoto.food import Food
from panzoto.utils import log_output


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
        self.status = None
        self.check_status()

    def eat_food(self,
                 food: Food) -> str:
        """Simulate eating behavior with person and food

        Args:
            food (Food): Food object

        Returns:
            str: output string
        """

        output = ""

        need = 10 - self.energy
        if food.food_value < need:
            self.energy += food.food_value
            food.food_value = 0
            output += f"{self.name} ate some {food.name}. But they are still " \
                       "hungrey."
        else:
            self.energy += need
            food.food_value -= need
            output += f"{self.name} ate some {food.name}. And they are no " \
                       "longer hungrey."

        return output

    def get_food_list(self) -> List[Food]:
        """List all of food a person have

        Returns:
            List[Food]: All the times in a person's possession
        """

        food_list = []
        for item in self.possession:
            if item.type == ThingStatus.FOOD.value:
                food_list.append(item)
        return food_list

    def eat(self) -> None:
        """Simulate eating if there is food in possession
        """
        food_list = self.get_food_list()
        if food_list:
            food = random.choice(food_list)
            self.eat_food(food)

    def __str__(self):
        return self.status

    def __repr__(self):
        return self.status

    def calc_expense(self) -> None:
        """Adjust health according energy. 
        More than 0 energy -> increase health to 10
        Less thatn 0 energy -> health decrease by 1
        """
        if self.energy <= 0:
            self.health -= 1 
        elif (self.energy > 0) and (self.health < 10):
            self.health += 1 
            self.energy -= 1
        else:
            self.energy -= 1 

    def calc_need(self) -> None:
        """Check if the person is hungery
        """
        if self.energy < CFG.hunger_check:
            self.eat()

    def check_death(self) -> None:
        """Check if the person will die. Random chance of dying. The older they
        are the more likely they are going to die.
        """
        chance = random.random()

        if (self.age / CFG.longest_life) > chance:
            self.alive = False

    def check_speed_multiplier(self) -> None:
        """This will adjust to the speed of the simulation using the "speed"
        parameter in config file
        """
        self.age += CFG.speed * 10

    def run_one_turn(self) -> None:
        """Chekc all the things for when a person runs one iteration
        """
        self.calc_need()
        self.calc_expense()
        self.check_status()
        self.check_death()
        self.check_speed_multiplier()

    def check_status(self) -> None:
        """Check and update the status of a person
        """
        if self.health <= 0:
            self.alive = False

        # updating status
        poss = []
        if self.possession:
            possession = [x.name for x in self.possession]
            poss = " ".join(possession)

        self.status = (
            f"{PersonStatus.FIRST_NAME.value}: {self.first_name}, "
            f"{PersonStatus.LAST_NAME.value}: {self.last_name}, "
            f"{PersonStatus.ID.value}: {self.uid}, "
            f"{PersonStatus.GENDER.value}: {self.gender}, "
            f"{PersonStatus.HEALTH.value}: {self.health}, "
            f"{PersonStatus.ENERGY.value}: {self.energy}, "
            f"{PersonStatus.POSESSION.value}: {poss}"
        )


def main():
    pass


if __name__ == "__main__":
    main()
