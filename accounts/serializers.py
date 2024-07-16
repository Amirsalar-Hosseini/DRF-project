from django.contrib.auth.models import User
from rest_framework import serializers


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin can\'t be in email')


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)}
        }

    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username can\'t be admin')
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('passwords do not match')
        return data