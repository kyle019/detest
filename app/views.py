from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseNotFound
from .crud import get_users, get_user, create_user, check_user_existence, get_users_by_ids
import requests
from django.views.decorators.csrf import csrf_exempt

def root(request):
    return redirect('/allUsers/')

def all_users(request):
    users = get_users()
    user_list = [{"id": user.id, "name": user.name} for user in users]
    return JsonResponse(user_list, safe=False)

def user_detail(request, user_id):
    user = get_user(user_id)
    if user is None:
        return HttpResponseNotFound('User not found')
    return JsonResponse({"id": user.id, "name": user.name})

@csrf_exempt
def create_user_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = create_user(name)
        return JsonResponse({"id": user.id, "name": user.name})

def check_user_existence_view(request, user_id):
    exists = check_user_existence(user_id)
    return JsonResponse({"exists": exists})

# def request_users(request, user_id):
#     url = f"http://localhost:8002/allUsers/"
#     response = requests.get(url)
#     response.raise_for_status()
#     subscription_data = response.json()
#     user_ids = subscription_data.get("id",[])
#     users = get_users_by_ids(user_ids)
#     user_list = [{"id": user.id, "name": user.name} for user in users]
#     return JsonResponse(user_list, safe=False)

def request_users(request, user_id):
    url = f"http://192.168.1.210:8002/subscription/magazine/{user_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        subscription_data = response.json()
        user_ids = subscription_data.get("usersId", [])
        users = get_users_by_ids(user_ids)
        user_list = [{"id": user.id, "name": user.name} for user in users]
        return JsonResponse(user_list, safe=False)

