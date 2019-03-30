from panzoto.Person import Person
import random
from panzoto.Utils import load_matrix

class Baby(Person):
    def __init__(self):
        mom, dad = self._born()
        super().__init__(mom.first_name, dad.last_name)

    def _born(self):
        matrix = load_matrix()
        people_dict = matrix.people_dict
        
        male_list = []
        female_list = []
        for key in people_dict:
            if people_dict[key].gender == 'FEMALE':
                female_list.append(key)
            elif people_dict[key].gender == 'MALE':
                male_list.append(key)
            else:
                print(f'Gender is undefined!')
        
        if male_list and female_list:
            mom = random.choice(female_list)
            dad = random.choice(male_list)
            return people_dict[mom], people_dict[dad]
        else:
            print("Was not able to find a mom and a dad!")
        