from django.db import models

# Create your models here.
class TaskManager(models.Manager):
    
    def getErrors(self, postData):
        errors = {}

        if len(postData["title"]) == 0:
            errors["title"] = "Title must not be blank."
        elif len(postData["title"]) < 3:
            errors["title"] = "Title must be at least 3 characters"
        
        if len(postData["description"]) < 10:
            errors["description"] = "Description must be at least 10 character."
        
        if len(postData["due_date"]) == 0:
            errors["due_date"] = "Due date must not be blank."
            
        return errors

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskManager()