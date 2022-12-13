from rest_framework.response import Response

from book.models import User, Source


def validate_signup(data):
    """
    Check if user_name or user_email is already taken.
    """
    name = data.get('user_name')
    email = data.get('user_email')
    error_message = {}

    is_user_taken = User.objects.filter(user_name=name)
    is_email_taken = User.objects.filter(user_email=email)

    if is_user_taken:
        error_message['user'] = 'The username already exists '
    if is_email_taken:
        error_message['email'] = 'This e-mail is being used'
    if error_message:
        return Response(error_message, status=409)
    return None


def validate_source(data):
    """
    Check if source_name already exists.
    """
    name = data.get('source_name')
    source = Source.objects.filter(source_name=name)
    if source:
        return Response('This source already exists.', status=409)
    return None
