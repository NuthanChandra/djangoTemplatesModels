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
    # The author used user_list = User.objects.order_by('first_name')
    # Followed by user_dict = {'users': user_list}
    users = User.objects.all()
    user_dict = {'users': users}
    return render(request, "second_app/users.html", context= user_dict)
