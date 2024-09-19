from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following') # Many-to-many relationship for following/followers, asymmetrical
    
    # String representation of the user
    def __str__(self):
        return self.username