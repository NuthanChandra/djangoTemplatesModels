from django import forms
from second_app.models import User

class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
class ModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
