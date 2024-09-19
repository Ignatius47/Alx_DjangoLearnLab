from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # For token creation

# Get the custom user model
User = get_user_model()

# Serializer for the User model (viewing user details)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'profile_picture', 'followers')

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Define password as a CharField to control validation and input type
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'bio', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is not returned in responses
        }

    # Override the create method to handle user creation
    def create(self, validated_data):
        # Use get_user_model().objects.create_user to create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),  # Optional field with default
            profile_picture=validated_data.get('profile_picture', None)  # Optional field with default
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
