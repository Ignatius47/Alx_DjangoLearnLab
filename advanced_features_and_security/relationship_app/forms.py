from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser, Post
from .models import Book

class CustomUserChangeForm(UserChangeForm):
    ROLES = [
        ('creator', 'Creator'),
        ('reader', 'Reader'),
    ]
    role = forms.CharField(choices=ROLES, required=True)
    class Meta(UserCreationForm.meta):
        model = CustomUser
        fields = '__all__'

# Define a form for creating and updating Post instances
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specify the model to use with this form
        fields = ['title', 'content', 'author']  # Fields to include in the form



class BookForm(forms.ModelForm):
    class Meta:
        app_label = 'relationship_app'
        model = Book
        fields = ['title', 'author', 'description', 'published_date', 'library']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'library': forms.Select(attrs={'class': 'form-control'}),
        }
