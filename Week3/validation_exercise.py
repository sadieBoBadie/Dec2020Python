# Create a function that takes a dictionary with these keys:
# title, description, due_date

# Validate:
# check to make sure that title, description and due-date
# values are not empty strings.
# Check to make sure title is at least 3 characters,
# description is at least 10 characters

# Error info:
# Return a dictionary with the only the keys
# that have any errors, and the value as a message 
# describing the error.

def validate(form_data):
    errors = {}
    # returns a dictionary with errors
    return errors

# Input (argument): 
# 
# {"title": "", "description": "ghjk", "due_date": "01/02/2021"}
# 
# Output (return): 
# {
#   "title": "Title cannot be blank"
#   "description: "Desc must have at least 10 characters",
# }