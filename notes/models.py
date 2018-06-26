from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


# Create your models here. -- This is where we define a class to say everything that our Note has

# https://docs.djangoproject.com/en/2.0/ref/models/class/
class Note(models.Model): # Note inherits all methods and logic from models.Model - TODO: read DOCs on this. link^
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # This is our reference to each instance of Note created which CANNOT be edited
    # TODO: Add user/author who created it
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # This will auto create the time when it is created
    last_modified = models.DateTimeField(auto_now=True) # This will update every time it is changed
    category = models.CharField(max_length=20) # 
    # TODO: Tagging system or categories

class PersonalNote(Note): # PersonalNote inherits all methods and logic from Note
  # A ForeignKey is a key that links the Primary Key of a different table
  # models.CASCADE will delete the User, and anything connected to it.  It's like a recursive deletion call.
  # Must be brought to admin.py and then you need to migrate
  user = models.ForeignKey(User, on_delete=models.CASCADE)