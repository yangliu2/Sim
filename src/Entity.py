import random

class Entity():
    def __init__(self, name):
        self.name = name
        self.id = random.randint(0, 1_000_000_000)