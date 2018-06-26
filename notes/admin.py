from django.contrib import admin
from notes.models import Note, PersonalNote # You can use import * IF you want to just import everything, but this is not convention.

# Register your models here.
admin.site.register(Note)
admin.site.register(PersonalNote)