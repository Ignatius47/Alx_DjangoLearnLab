from django.contrib import admin

# Register your models here.
from .models import Book
from django.contrib import admin
from .models import Book, Author, Librarian, Library
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('date_of_birth', 'profile_photo')}),)

admin.site.register(CustomUser, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title' , 'author')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
