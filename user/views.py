# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from core import log_data
from core.responses import exception_response
from user import serializers as user_ser
from user.service import UserManagementService

user_management_service = UserManagementService()


class UserSignup(APIView):
    @swagger_auto_schema(
        operation_id='User Signup',
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
                                    properties={
                                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                                        'password': openapi.Schema(type=openapi.TYPE_STRING),
                                        'confirm_pwd': openapi.Schema(type=openapi.TYPE_STRING)
                                    }
                                    ))
    def post(self, request):
        """
        :param request:
        :return: create a new user and return the details of user.
        """
        try:
            # user sign up serializer
            data = request.data
            serializer = user_ser.UserSignupSerializers(data=data)
            confirm_pwd = data.get('confirm_pwd')
            # user signup service
            return user_management_service.user_signup(serializer=serializer, confirm_pwd=confirm_pwd)
        except Exception as e:
            log_data.error(f'{e.__str__()}')
            return exception_response(e)


class UserSignIn(APIView):
    @swagger_auto_schema(
        operation_id='User Login',
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
                                    properties={
                                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                                        'password': openapi.Schema(type=openapi.TYPE_STRING),
                                    }
                                    ))
    def post(self, request):
        """
        :param request:
        :return: login a user fetch profile details of login user
        """
        try:
            # user login serializer
            serializer = user_ser.UserLoginSerializer(data=request.data)
            # user sign_in service
            return user_management_service.user_sign_in(serializer=serializer)
        except Exception as e:
            log_data.error(f'{e.__str__()}')
            return exception_response(e)

    def get(self, request, user_id):
        """
        :param user_id:
        :param request:
        :return:
        """
        try:
            return user_management_service.get_profile_details(pk=user_id)
        except Exception as e:
            log_data.error(f'{e.__str__()}')
            return exception_response(e)
