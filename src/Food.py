from src.Thing import Thing

class Food(Thing):

    def __init__(self, name, value):
        super().__init__(name.capitalize(), value)

    def __str__(self):
        return f'Name: {self.name}, Value: {self.value}'
        
    def __repr__(self):
        return f'Name: {self.name}, Value: {self.value}'