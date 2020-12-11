from django.db import models

# Create your models here.

# Create a facebook wall - Only the wall feature with posts and comments
# (except likes, as this will be covered in the many-to-many section)
# What tables would you need in your database?
# What Models would you need?
# What relationships would they have to each other?

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # posts
    # comments

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    # comments

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

#                                   One     many
# A user can post many posts ##   User --> posts [X]
# A user can post many comments   User --> comments [X]
# A post can have many comments   Post ---> comments
# A comment can only have one post it belongs to.                               







# One-to-Many Example
# One author can write many books, a book can have one author

# class Author(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     # books = list of all the books

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

# Many-to-Many Example
# A book can have multiple authors, and an author can co-author or author many books.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # books = list of all the books

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name="books")