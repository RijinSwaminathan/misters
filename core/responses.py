from rest_framework import status
from rest_framework.response import Response


def exception_response(e):
    return Response(
        {
            'status': 403,
            'error': e.__str__()
        },
        status=status.HTTP_403_FORBIDDEN
    )


def invalid_serializer(serializer):
    return Response(
        {
            'status': 400,
            'message': 'something went wrong',
            'error': serializer.errors,
        },
        status=status.HTTP_400_BAD_REQUEST
    )


def signup_complete(user, token):
    return Response(
        {
            'status': 201,
            'message': 'signup successfully',
            'user_id': user.id,
            'user_name': user.username.__str__(),
            'token': token[0].key,
        },
        status=status.HTTP_201_CREATED)


def signin_complete(user, token):
    return Response(
        {
            'status': 200,
            'message': 'user sign in completed successfully',
            'user_id': user.id,
            'user_name': user.username.__str__(),
            'token': token[0].key,
        },
        status=status.HTTP_200_OK)


def invalid_password():
    return Response(
        {
            'status': 406,
            'message': 'passwords are not matching',
        },
        status=status.HTTP_406_NOT_ACCEPTABLE
    )


def get_profile(user_detail):
    return Response(
        {
            'status': 200,
            'message': 'get the profile details successfully',
            'user_data': user_detail.data
        },
        status=status.HTTP_200_OK

    )


def user_not_exist():
    return Response(
        {
            'status': 404,
            'message': 'user not exist',
        },
        status=status.HTTP_404_NOT_FOUND
    )
