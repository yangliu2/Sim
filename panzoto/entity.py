import random
import uuid

class Entity():
    def __init__(self, name):
        self.name = name
        self.uid = uuid.uuid4()

    def __eq__(self, other):
        return self.uid == other.uid