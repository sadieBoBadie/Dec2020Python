from django.db import models

# 1
# Create the models.py for a Dungeons and Dragons sign up

# Users can create campaigns as the Dungeon Master
# Users can join campaigns as players
# Campaigns can have many players

class DnDUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # whatever other fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # dm_campaigns
    # player_campaigns

class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255)
    # whatever other fields
    dungeon_master = models.ForeignKey(DnDUser, related_name="dm_campaigns")
    players = models.ForeignKey(DnDUser, related_name="player_campaigns")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# 2
# Create the models.py for a book lending app

# Users can post books to lend
# Users can borrow books from other users.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # whatever other fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # books_to_lend
    # borrowed_books

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # whatever other fields/relationships
    owner = models.ForeignKey(User, 
        related_name="books_to_lend",
        on_delete=models.CASCADE,
        )
    borrower = models.ForeignKey(User, 
        related_name="borrowed_books",
        on_delete=models.SET_NULL,
        null=True
        )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
