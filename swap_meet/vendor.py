# wave 1
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
#wave 2
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        else:
            return None


#wave 3
    def swap_items(self,other_vendor, my_item, their_item):
        if ((my_item not in self.inventory) or
            (their_item not in other_vendor.inventory)):
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)

        return True   
    
#wave 4

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        # self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        temp = None
        temp = other_vendor.inventory[0]
        other_vendor.inventory[0] = self.inventory[0] 
        self.inventory[0]  = temp

        return True

