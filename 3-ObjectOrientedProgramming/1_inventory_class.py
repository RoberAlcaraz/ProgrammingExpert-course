# INVENTORY CLASS
# Write an Inventory class, as defined below, that handles the
# management of inventory for a company. All instances of this class should be
# initialized by passing an integer value named max_capacity  that
# indicates the maximum number of items that can be stored in inventory. Your
# Inventory  class will need to store items that are represented
# by a name, price and quantity. Your class should implement the following methods:

# - add_item(name, price, quantity), : This method should add an
#   item to inventory and return True  if it was successfully
#   added. If adding an item results in the inventory being over capacity your
#   method should return False  and omit adding this item to the
#   inventory. Additionally, if an item with the passed name
#   already exists in inventory this method should return False  to indicate
#   the item could not be added.

# - delete_item(name), : This method should delete an item from
#   inventory and return True  if the item was successfully
#   deleted. If there is no item with the passed name  this method
#   should return False.

# - get_most_stocked_item(), : This method should return the name
#   of the item that has the highest quantity in the inventory, and return
#   None  if there are no items in the inventory. You may assume
#   there will always be exactly one item with the largest quantity, except
#   for the case where the inventory is empty.

# - get_items_in_price_range(min_price, max_price), : This method
#   should return a list of the names of items that have a price within the
#   specified range (inclusively).

class Inventory:

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        # self.names['price'] = []
        # self.names['quantity'] = []
        self.n_items = 0

    def add_item(self, name, price, quantity):
        if self.n_items + quantity <= self.max_capacity:
            if name in self.items.keys():
                return False

            self.items[name] = {}
            self.items[name]['price'] = price
            self.items[name]['quantity'] = quantity
            self.n_items += quantity
            return True

        return False

    def delete_item(self, name):

        if name in self.items.keys():
            self.n_items -= self.items[name]['quantity']
            del self.items[name]
            return True

        return False

    def get_most_stocked_item(self):
        most_stocked_item = None
        q = 0
        for name, values in self.items.items():
            if values['quantity'] > q:
                q = values['quantity']
                most_stocked_item = name

        return most_stocked_item

    def get_items_in_price_range(self, min_price, max_price):
        items_in_range = []
        for name, values in self.items.items():
            if min_price <= values['price'] <= max_price:
                items_in_range.append(name)

        return items_in_range


inventory = Inventory(4)
print(inventory.add_item('Chocolate', 4.99, 3))
print(inventory.add_item('Bread', 4.99, 1))
print(inventory.get_most_stocked_item())
print('--------------------------------------')

inventory = Inventory(4)
inventory.add_item('Chocolate', 4.99, 4)
inventory.delete_item('Chocolate')
inventory.delete_item('Chocolate')
inventory.delete_item('Bread')
print(inventory.n_items)
inventory.add_item('Chocolate', 4.99, 2)
inventory.add_item('Bread', 4.99, 2)
print(inventory.items)
print('--------------------------------------')
print(inventory.get_most_stocked_item())
print('Chocolate' in ('Chocolate', 'bread'))
print('--------------------------------------')


print('--------------------------------------')
print(('Chocolate', 'Bread') == ('Chocolate', 'Bread'))
print('--------------------------------------')
print(inventory.add_item('Chocolate', 4.99, 4))
print(inventory.add_item('Butter', 4.99, 1))
print(inventory.add_item('Butter', 4.99, 1))
print(inventory.add_item('Butter', 4.99, 1))
print(inventory.add_item('Bread', 4.99, 2))
print(inventory.add_item('W', 4.99, 2))

print(inventory.get_most_stocked_item())
