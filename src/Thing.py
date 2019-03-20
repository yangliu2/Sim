from src.Entity import Entity

class Thing(Entity):

    def __init__(self, name, value, category):
        super().__init__(name)
        self.max_value = value
        self.value = value
        self.type = category
        self.owner = None