# Import necessary modules and classes from Django REST Framework and the datetime module
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    # Authors can be serialized as a list of authors related to the book
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all(), read_only=False)

    class Meta:
        # Specify the model to be serialized
        model = Book
        # Serialize all fields in the Book model, including the authors field
        fields = '__all__'

    # Custom validator for the publication year field
    def validate_publication_year(self, value):
        # Get the current year
        current_year = datetime.now().year
        # Check if the provided publication year is in the future
        if value > current_year:
            # If it's in the future, raise a validation error
            raise serializers.ValidationError("Publication year cannot be in the future.")
        # If the year is valid, return the value
        return value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # If an Author has multiple books, you can use the 'many=True' option to serialize them
    books = BookSerializer(many=True, read_only=True)  # Add this to serialize the related books

    class Meta:
        # Specify the model to be serialized
        model = Author
        # Serialize all fields in the Author model, including related books
        fields = '__all__'
