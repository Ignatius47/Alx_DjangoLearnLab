from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

# New form as per task requirements
class ExampleForm(forms.Form):
    # Define some example fields for demonstration purposes
    name = forms.CharField(max_length=100, help_text="Enter your name")
    email = forms.EmailField(help_text="Enter your email address")
    message = forms.CharField(widget=forms.Textarea, help_text="Enter your message")
