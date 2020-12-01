#1.
# OOP:
# Avoid repeated code / Reusability
# Cleaner/ Organization / Modularization
# Maintaining code / Data uniformity

# 2:
# What is CLASS:
# # Cookie cutter, blue print
# # Custom datatypes

# 3.
# Attributes/properties --- variable that belongs to an instance - "What it has"
# Methods --- "Actions that an object can do" --- 
#     functions that every instance of that class can do!

arr =[4, 5, 6, 7]
arr.pop()
arr.append(3)

# Quiz Challenge:

# self.store = store
# self.items.append(item)   
# def add_item(self, item, price):   
# self.items = []
# def __init__(self, store):
# class ShoppingCart:
# return self
# self.total = 0
# self.total += price

class ShoppingCart:

    # Constructor
    def __init__(self, store):
       self.store = store
       self.items = []
       self.total = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
        return self

sadie_shopping_cart = ShoppingCart("Safeway")
print(sadie_shopping_cart)
print(sadie_shopping_cart.store)

nate_cart = ShoppingCart("Target")
print(nate_cart)
print(nate_cart.store)

nate_cart.store = "Amazon"

nate_cart.add_item("Star Wars Figurine", 50.00)
nate_cart.add_item("apple", 0.99)
