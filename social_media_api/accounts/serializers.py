from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # Import Token for token authentication

# Get the custom user model
User = get_user_model()

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'profile_picture', 'followers')  # Corrected 'prrofile_picture' to 'profile_picture'

# Serializer for registering a new user
class RegisterSerializer(serializers.ModelSerializer):
    # Use CharField for password to ensure it is treated as a string and add validation rules
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})  # Password field should not be readable

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    # Overriding the create method to handle user creation
    def create(self, validated_data):
        # Use get_user_model().objects.create_user to create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),  # Defaults to an empty string if not provided
            profile_picture=validated_data.get('profile_picture', None)  # Defaults to None if not provided
        )

        # Create a token for the new user
        Token.objects.create(user=user)

        return user
