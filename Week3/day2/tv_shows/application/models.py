from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def validateShow(self, postData):
        errors = {}

        if len(postData["release_date"]) == 0:
            errors["release_date"] = "Release date must not be blank."
        
        if len(postData["title"]) == 0:
            errors["title"] = "Title is required."
        elif len(postData["title"]) < 2:
            errors["title"] = "Title must be at least 2 characters."

        if len(postData["network"]) == 0:
            errors["network"] = "Network is required."
        elif len(postData["network"]) < 3:
            errors["network"] = "Network must be at least 3 characters."

        if len(postData["description"]) == 0:
            errors["description"] = "Desc is required."
        elif len(postData["description"]) < 10:
            errors["description"] = "Desc must be at least 2 characters."
        
        showExists = Show.objects.filter(title=postData["title"])
        
        if showExists:
            errors["title_exists"] = "Show already in db!"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __repr__(self):
        return f"Show: {self.title} {self.network}"
    