from django.contrib import admin

# Register your models here.


from.models import book_DB,book_DBAdmin
admin.site.register(book_DB,book_DBAdmin)