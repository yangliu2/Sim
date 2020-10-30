""" Matrix object to create the world """

from uuid import UUID
from panzoto.person import Person
from panzoto.baby import Baby
from panzoto.food import Food
from panzoto.utils import log_output


class Matrix():

    def __init__(self):
        self.people_dict = {}
        self.thing_dict = {}

    @staticmethod
    def get_full_name(first_name: str,
                      last_name: str) -> str:
        """Generate the name of the person as a continous string

        Args:
            first_name (str): first name
            last_name (str): last name

        Returns:
            str: full name in continous string
        """
        return f'{first_name.capitalize()}_{last_name.capitalize()}'

    @log_output
    def create_person(self, 
                      first_name: str, 
                      last_name: str) -> str:
        """create a person using first and last name

        Args:
            first_name (str): first name    
            last_name (str): last name

        Returns:
            str: all the output in from the function
        """

        output = ""

        person = Person(first_name, last_name)
        output += f'{person.name} created.'
        self.people_dict[person.uid] = person

        return output

    @log_output
    def delete_person(self, 
                      uid: str) -> str:
        """Remove a person from the matrix using uid string

        Args:
            uid (str): uuid string

        Returns:
            str: output from this function
        """

        output = ""

        id = UUID(uid)
        if id in self.people_dict:
            del self.people_dict[id]
        else:
            output += 'That person does not exist!'

        return output

    def create_baby(self):
        baby = Baby()
        self.people_dict[baby.uid] = baby

    @log_output
    def list_people(self):
        output = ""
        if not self.people_dict:
            output += 'No people exist.'

        for person in self.people_dict:
            output += f'{self.people_dict[person].name}\n'
        
        return output

    @log_output
    def show_person(self, 
                    first_name: str, 
                    last_name: str) -> str:
        """Show info about a specific person

        Args:
            first_name (str): first name
            last_name (str): last name

        Returns:
            str: output of this function
        """
        output = ""
        name = self.get_full_name(first_name=first_name,
                                  last_name=last_name)
        target_list = [str(self.people_dict[x]) for x in self.people_dict
                       if name == self.people_dict[x].full_name]

        if target_list:
            output += "\n".join(target_list)
        else:
            output += f'Cannot find the person you are searching.'
        
        return output

    def assign_item(self, thing, first_name, last_name):
        person = self.get_full_name(first_name=first_name,
                            last_name=last_name)
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
            print(f"Neither that person nor the thing exist!")

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
