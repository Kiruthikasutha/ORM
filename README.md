# Ex02 Django ORM Web Application
## Date: 28.2.24

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<web 1.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import book_DB,book_DBAdmin
admin.site.register(book_DB,book_DBAdmin)

models.py




from django.db import models
from django.contrib import admin
class book_DB(models.Model):
    book_name=models.CharField(max_length=20);
    author=models.CharField(max_length=20);
    published_year=models.IntegerField();
    bookno=models.IntegerField(primary_key = "bookno");
    bookrate=models.IntegerField();
class book_DBAdmin(admin.ModelAdmin):
    list_display=("book_name","author","published_year","bookno","bookrate")
```

## OUTPUT

![output](<Screenshot 2024-02-28 093513.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
