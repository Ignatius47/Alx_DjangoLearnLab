# Generated by Django 5.1 on 2024-08-23 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_alter_book_options_remove_library_author_librarybook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='librarybook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.RemoveField(
            model_name='librarian',
            name='library',
        ),
        migrations.RemoveField(
            model_name='librarybook',
            name='library',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='LibraryBook',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
