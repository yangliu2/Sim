from src.Thing import Thing

class Food(Thing):

    def __init__(self, name, value):
        super().__init__(self, name, value)

    def __str__(self):
        if self.value == self.max_value:
            return f'A fresh {self.name}'
        elif self.value < (self.max_value / 2):
            return f'A half aten {self.name}'
        
    def __repr__(self):
        return f'Name: {self.name}, Value: {self.value}'