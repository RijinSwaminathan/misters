from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User


class UserSignupSerializers(serializers.Serializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True)

    def sign_up(self, username, password):
        try:
            return User.objects.signup(username=username,
                                       password=password)
        except Exception as e:
            raise serializers.ValidationError(e.__str__())


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ProfileDetailsSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
