from django.db import transaction
from rest_framework.authtoken.models import Token

from core import log_data
from core import responses as message
from user.models import User
from user.serializers import ProfileDetailsSerializer


class UserManagementService:
    @transaction.atomic()
    def user_signup(self, serializer, confirm_pwd):
        if serializer.is_valid(raise_exception=True):
            # get the username from user
            username = serializer.data.get('username')
            # get the password from user
            password_ = serializer.data.get('password')
            # match the confirmed password and password
            log_data.warning(f'enter the passwords correctly')
            if confirm_pwd == password_:
                user = serializer.sign_up(username=username,
                                          password=password_)
                token = Token.objects.get_or_create(user=user)
                log_data.info(f'Sign-up operation completed')
                # responses are stored in a common file
                return message.signup_complete(user, token)
            else:
                log_data.error(f'passwords are not matching')
                return message.invalid_password()

    @transaction.atomic()
    def user_sign_in(self, serializer):
        if serializer.is_valid(raise_exception=True):
            user_name = serializer.data.get('username')
            password = serializer.data.get('password')
            if User.objects.filter(username=user_name):
                user = User.objects.get(username=user_name)
                if user.check_password(password):
                    token = Token.objects.get_or_create(user=user)
                    user.save()
                    log_data.info(f'user sign in completed')
                    return message.signin_complete(user, token)
                else:
                    log_data.error(f'Invalid user password')
                    return message.invalid_password()
            else:
                log_data.error(f'User does not exists')
                return message.user_not_exist()

    def get_profile_details(self, pk):
        user_data = User.objects.get(pk=pk, is_delete=False, is_active=True)
        if user_data:
            user_detail = ProfileDetailsSerializer(user_data, many=False)
            return message.get_profile(user_detail)
        else:
            log_data.error(f'User does not exists')
            return message.user_not_exist()
