from uuid import uuid4

#import swap_meet.vendor

#wave 2


class Item:
    def __init__(self, id = None):
        self.id = uuid4().int if id is None else id

    def get_category(self):
        return "Item" #returnig class as a string


#wave 3 
    def __str__(self):
        return f"An object of type Item with id {self.id}." # same as get_category, there maybe hard code issue