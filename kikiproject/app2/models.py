


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