from .models import User
from django.http import JsonResponse

def get_users():
    users = User.objects.all()
    return users

def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None

def create_user(name):
    user = User(name=name)
    user.save()
    return user

def check_user_existence(user_id):
    return User.objects.filter(id=user_id).exists()

from .models import User

def get_users_by_ids(user_ids):
    users = User.objects.filter(id__in=user_ids)
    return users