from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hola amigos")

# def app_index(request):
#     dict = {'ho': "Guten tag"}
#     return render(request, "second_app/index.html", context=dict)

def users(request):
    users = User.objects.all()
    user_email = []
    for user in users:
        user_email.append({'first_name': user.first_name, 'email': user.email})
    user_dict = {'user_email': user_email}
    return render(request, "second_app/users.html", context= user_dict)
