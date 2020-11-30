# Python

# [X] Virtual Environment
# [X] Version
# [X] Print
print("hello")
# [X] f-strings
greeting = "Hello, "
name = "Michael"
# [X] variables
# [X] Data Types
# [X] Primitive
    # int integer / float
# num = 5
# num2 = 5.0
# num3 = num + num2

# boolean
isDrinkingAge = True

# strings --- immutable
name = "Sodie"
name = name + " Flick"
print(name)
# name[1] = "a" --> will throw an error

# [X] Composite (data types that hold multiple values)
   # list (just like arrays)
nums = [2, 3, 4, 5]
   # dictionary - like objects - key, value pairs

student = {
    "first_name": "Michael",
    "last_name": "Shin",
    "birthday": "11/22"
}

students = [
    {
        "first_name": "Michael",
        "last_name": "Shin",
        "birthday": "11/22"
    },
    {
    "first_name": "Joe",
    "last_name": "Lee",
    "birthday": "09/03"
    }
]
print(students[0]["last_name"]) # Shin

# [ ] whitespace
#   ---> scope within if statements, for loops, 
#        or other scopes, and later class definitions
#        require indentation - 
#   ---> must be either all same amount of spaces, 
#        or tabs. Cannot mix spaces and tabs.
#   ---> Note VS code inserts 4 spaces when you press tab.


# [ ] Conditionals
age = 21

if age > 20:
    print("Come to happy hour!!")
elif age <= 20:
    print("Sorry, see you lata sucka!")
else:
    print("this is unreachable code!")

# [ ] Loops

# All three do the same thing:
#      start // exclusive end // step (add 1 in this case)
for i in range(0, 12, 1):
    print(i)

#        start  // exclusive end // (step/increment defaults to 1)
for num in range(0, 12):
    print(i)

#        exclusive end // (start defaults to 0, step/increment defaults to 1)
for everyInt in range(12):
    print(i)

# [ ] Functions

def greetByAge(age):

    if age > 20:
        print("Come to happy hour!!")
    elif age <= 20:
        print("Sorry, see you lata sucka!")
    else:
        print("this is unreachable code!")

your_age = 21
greetByAge(your_age)