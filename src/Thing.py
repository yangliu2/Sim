from src.Entity import Entity

class Thing(Entity):

    def __init__(self, name, value):
        super().__init__(name)
        self.max_value = value
        self.value = value