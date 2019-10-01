from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
from second_app import forms

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

def user_form(request):
    form = forms.ModelForm()
    if request.method == 'POST':
        form = forms.ModelForm(request.POST)
        if form.is_valid():
            user_data = User()
            user_data.first_name = form.cleaned_data['first_name']
            user_data.last_name = form.cleaned_data['last_name']
            user_data.email = form.cleaned_data['email']
            user_data.save()
            return index(request)
    return render(request, 'second_app/user_form.html', {'form': form})
