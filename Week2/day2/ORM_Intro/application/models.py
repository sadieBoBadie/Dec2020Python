from django.db import models

# Create your models here.
#  Model        View          Controller

# Model     Template           Views
#  DB?     | what user sees   |   logic

# Object Relational Mapping
# OOP

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add =True)
    
    # objects  -> Manager class
    # save()


    # CREATE
    #   User.objects.create()
    # READ
    #   make a variable!!
    #   all_users = User.objects.all() ---> list of objects
    #   User.objects.get() ---> User instance/object
    #   User.object.filter() ---> list of objects
    # UPDATE
    #   # make a variable for the User
    #   # update that variable's attributes
    #   # user2.save()