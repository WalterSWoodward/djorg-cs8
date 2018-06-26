# Setting up BASIC django app:
# Day 1:

## Initial Setup:

In terminal run:

    pipenv --three
    pipenv shell
    pipenv install django
    django-admin startproject djorg . # period here is VERY important!
    django-admin startapp notes` # in same base folder, no need to cd

To run/open server # "./" in linux just means "run this program"

    * [```python manage.py runserver``` also works.]
    ```./manage.py runserver```

Shows all migrations

    ./manage.py showmigrations

Tells us the sql commands that it is building for us to set up our database and move all the data over.

    ./manage.py sqlmigrate admin 0001_initial
    -- remembe that relational databases are the ones with `keys` that allow you to connect different data together e.g. Users with User Comments.
    `./manage.py migrate`
    `./manage.py shell` - to exit: use `exit()` or CTRL D

How do we deal with our secret key issue in djorg/settings.py? How do we keep it secure?

    `pipenv install python-decouple`

setup included bringing in library:

Then setting up .env with SECRET_KEY
gitignore by default has .env so you are now good to commit
check git status just to be sure that env is not being sent up


## Create Notes App:

Use UUID to generate keys to identify Notes -- UUID is basically a unqiue randomly generated string

Once this is setup:

    `./manage.py runserver` # Just to check that it works

Then we need to add `notes` to INSTALLED_APPS in settings.py. 

    `./manage.py showmigrations` # Shows that there are no migrations for notes
    `./manage.py makemigrations` # look around and see if there is anything you need to migrate
    `./manage.py migrate` # adds migrations to notes

Create an Instance in the shell and take a look at what you can do with it

    `./manage.py shell`

Inside shell

    `./manage.py shell`
        `from notes.models import Note`
        `n = Note(title='example', content = 'this is a test')`
        `n.title` -- returns the title
        `n.content`
        `n.id`
        `print(n.__dict__)` -- prints everything
        `n.content = 'this is a test 2'`
        `n.content` -- returns ^
        `n.save()`
        `exit()`
    `./manage.py shell` # inside the shell again
        `from notes.models import Note`
        `Note.objects.all()`
        `b = Note.objects.all()`
        `print(b.__dict__)`
        `b[0]`

# Day 1 Assignment:

-- Use django-admin to create a new app
-- Do the same thing except instead of notes, for bookmarks
-- id, name for the bookmark, web-addresses for the link, notes (optional), created-at, last-modified

## Create Bookmark App:

    `django-admin startapp bookmarks`

In the same base repo folder (no need to `cd django-admin startapp bookmarks`)

    `./manage.py runserver`

You should be able to see that the server is running fine

    `./manage.py showmigrations`

Should see that bookmarks is not on the list yet

This command is like a history of your sql commands:   

    `./manage.py sqlmigrate bookmarks 0001_initial`

Typing:
    
    `./manage.py migrate`

Terminal will say -> `No migrations to apply` b/c `bookmarks` is not in `INSTALLED_APPS` in settings.py yet - do that!

Entering `./manage.py showmigrations` will show that there are no migrations for bookmarks.

    ./manage.py makemigrations # searches files for new code to migrate

    ./manage.py migrate

Now you can create instances of the models:

    `./manage.py shell`
        `from bookmarks.models import Bookmark`
        `n = Bookmark(title='bookmark1', description = 'describes bookmark1', url = 'https://www.google.com')`
        `n.title` -- returns the title
        `n.description`
        `n.id`
        `n.url`
        `print(n.__dict__)` # prints everything
        `n.content = 'this is a test 2'`
        `n.content`
        `n.save()`
        `exit()`

Ran into some issues so I just deleted the database following these instructions:

- Delete the sqlite database file (often db.sqlite3) in your django project folder (or whereever you placed it)
- Delete everything except **init**.py file from migration folder in all django apps
- Make changes in your models (models.py).
- Run the command python manage.py makemigrations or python3 manage.py makemigrations
- Then run the command python manage.py migrate.

Then created new instances of both Bookmark and Note:

    `from bookmarks.models import Bookmark`
    `new_bookmark = Bookmark(title="Yahoo", description="search stuff here", url="http://www.yahoo.com")`
    `from notes.models import Note`
    `new_note = Note(title="Grocery List", content="Cabbage, Corn Beef, Green Clothes")`

`create_at` and `last_modified` can only be tested AFTER you run `.save()`:

    `new_note.save()`

Now created_at is defined, but last_modified will be the same value

    `new_note.content += ', Matches'`

Now last_modified is updated, check it:

    `new_note.create_at`
    `new_note.last_modified`

Everything works!

# Day 2

    pipenv shell
    ./manage.py runserver

Now navigate to:
localhost:8000/admin

To get started, we need to look at manage.py: lots of abstracted code

    ./manage.py createsuperuser

Create a new user with limited access

    from .models import Note in admin.py
    admin.site.Register(Note)

Input in your Note model:

    category = models.CharField(max_length=20)

In terminal:

    `python manage.py makemigrations`
    1
    'default'

In terminal:

    python manage.py migrate

## Django Database Under the Hood:

To actually look at the django database("under the hood"):
./manage.py dbshell

Take a look at the tables:
.tables

You can see all the tables we have, those we created like (note_note, notes_personalnote, bookmarks_bookmark), and those we didn't. We saw these in our initial migration.

    .headers on
    .mode column

With SQL you have to use a semi-colon...if you don't it will show ..> prompting you to add a more to your command.
    `SELECT * FROM notes_note;`
    `SELECT * FROM notes_note;`

DO NOT TYPE THIS IN:  As an example, if <COMMAND HERE> -- FINISH THIS





