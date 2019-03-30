from panzoto.Thing import Thing

class Food(Thing):

    def __init__(self, name, value):
        super().__init__(name.capitalize(), int(value), 'FOOD')

    def __str__(self):
        return f'{self.name}'
        
    def __repr__(self):
        return f'{self.name}'

