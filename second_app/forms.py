from django import forms
from second_app.models import User

class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
class NewUserForm(forms.ModelForm): 
    class Meta():
        model = User
        fields = '__all__'
