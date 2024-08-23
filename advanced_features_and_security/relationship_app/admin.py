from django.contrib import admin
from .models import Book, Author, Librarian, Library
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('date_of_birth', 'profile_photo')}),)

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', )
