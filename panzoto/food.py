from panzoto.thing import Thing
from panzoto.enums import FoodStatus, ThingStatus


class Food(Thing):

    def __init__(self, name, value):
        super().__init__(name=name.capitalize(), 
                         value=0, 
                         category=ThingStatus.FOOD.value)
        self.food_value = value
        self.food_worth = True
        self.status = None
        self.check_status()

    def __str__(self):
        return self.status
        
    def __repr__(self):
        return self.status

    def check_status(self):
        """Check and update the status of the food item
        """
        if self.food_value <= 0:
            self.food_worth = False
        
        self.status = (
            f"{FoodStatus.ID.value}: {self.uid}, "
            f"{FoodStatus.NAME.value}: {self.name}, "
            f"{FoodStatus.OWNER.value}: {self.owner}, "
            f"{FoodStatus.FOOD_VALUE.value}: {self.food_value}"
        )
