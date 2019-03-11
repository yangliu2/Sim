from src.Entity import Entity

class Person(Entity):

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        super().__init__(f'{self.first_name}_{self.last_name}')

        self.age = 0
        self.gender = None
        self.dad = None
        self.mom = None
        self.health = 0
        self.energy = 0
        self.aptite = 0 # 1-10, hungry to full

    def eat(self, food):
        if self.energy > 10:
            print(f'Full.')
        else:
            need = 10 - self.energy
            if food.value < need:
                self.energy += food.value
                food.value = 0
                print(f'{self.name} ate some {food.name}. But they are still hungrey.')
            else:
                self.energy += need
                food.value -= need
                print(f'{self.name} ate some {food.name}. And they are no longer hungrey.')
    
    def __str__(self):
        return f'First name: {self.first_name}, Last Name: {self.last_name}, Energy: {self.energy}'

    def __repr__(self):
        return f'First name: {self.first_name}, Last Name: {self.last_name}, Energy: {self.energy}'

def main():
    pass

if __name__ == "__main__":
    main()