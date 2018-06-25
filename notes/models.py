from django.db import models
from uuid import uuid4

# Create your models here. -- This is where we define a class to say everything that our Note has

# https://docs.djangoproject.com/en/2.0/ref/models/class/
class Note(models.Model): # Note inherits all methods and logic from models.Model - TODO: read DOCs on this. link^
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # This is our reference to each instance of Note created which CANNOT be edited
    # TODO: Add user/author who created it
    # author = models.
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # This will auto create the time when it is created
    last_modified = models.DateTimeField(auto_now=True) # This will update every time it is changed
    # TODO: Tagging system or categories
