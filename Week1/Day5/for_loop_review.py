# for i in range(0, 10, 1):
#     print(i)

# print("*"*15)

# fruits = ["apples", "mangoes", "durians", "kiwis"]

# for i in range(len(fruits)):
#     print(fruits[i])

# print("*"*15)

# for fruit in fruits:
#     print(fruit)

# print("*"*15)


class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

users = [
    User("Jim", "Reeder"), 
    User("Emilie", "Wu"), 
    User("John", "Williams")
]

# for val in some_list
for user in users:
    print(user.first_name)

user_info = {
    "first_name": "Valerie", 
    "last_name": "Kirby",
    "email": "v@v.com"
}

# for key in some_dict
for val in user_info.values():
    print(val)