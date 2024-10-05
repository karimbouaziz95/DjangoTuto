from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)                 # Fields names of the model (in a tuple)
    prepopulated_fields = {"slug": ("title", )}  # The value is a tuple holding all the fields used for that field (slug)
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
