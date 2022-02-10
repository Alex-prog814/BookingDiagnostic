from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from applications.user.models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation')

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with given email already exists')
        return email

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords don\'t match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(email, password)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    auto = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = UserProfile
        fields = ('id', 'full_name', 'auto')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        user_profile = UserProfile.objects.create(**validated_data)
        return user_profile
