from uuid import uuid4
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, id = None, fabric = None, condition = 0):
        super().__init__(id = id, condition = condition)

        self.fabric = fabric if fabric else "Unknown"

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    