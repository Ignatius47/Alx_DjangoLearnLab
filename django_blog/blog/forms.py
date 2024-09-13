from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' here

    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.request.user  # Assuming request.user is available in the view
        if commit:
            post.save()
            self.save_m2m()  # For saving many-to-many relations like tags
        return post

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Ensure request is passed to the form
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        comment = super().save(commit=False)
        if self.post:
            comment.author = self.request.user
        comment.save()
        return comment
