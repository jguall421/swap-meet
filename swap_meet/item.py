from uuid import uuid4
#import swap_meet.vendor

class Item:
    def __init__(self, id = None):
        self.id = uuid4().int if id is None else id

    def get_category(self):
        return "Item" #returnig class as a string





