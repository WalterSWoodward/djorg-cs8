from django.db import models
from uuid import uuid4

# Create your models here.

class Bookmark(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) # This will auto create the time when it is created
    last_modified = models.DateTimeField(auto_now=True) # This will update every time it is changed
    
