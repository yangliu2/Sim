""" Babies are when Person starts from the beginning """

from panzoto.person import Person
from typing import Tuple
import random
from panzoto.utils import load_matrix, timer, log
from panzoto.enums import Gender, Logging

class Child(Person):
    def __init__(self,
                 mom: Person,
                 dad: Person):
        super().__init__(mom.first_name, dad.last_name)
        log(text=f"A baby named {mom.first_name} {dad.last_name} was born.",
            level=Logging.INFO.value)

    @timer
    def _born(self) -> Tuple[Person, Person]:
        # TODO: consider delete if not using anymore
        """Simulate the born process. Choose random mom and dad.

        Returns:
            Tuple[Person, Person]: Two person objects: mom and dad
        """
        matrix = load_matrix()
        people_dict = matrix.people_dict
        
        male_list = []
        female_list = []
        for key in people_dict:
            if people_dict[key].gender == Gender.FEMALE.value:
                female_list.append(key)
            elif people_dict[key].gender == Gender.MALE.value:
                male_list.append(key)
            else:
                log(text=f'Some gender are undefined',
                    level=Logging.ERROR.value)

        if male_list and female_list:
            mom = random.choice(female_list)
            dad = random.choice(male_list)
            return people_dict[mom], people_dict[dad]
        else:
            log(text=f"Was not able to find a mom and a dad!",
                level=Logging.INFO.value)

        