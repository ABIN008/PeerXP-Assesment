from django import forms
from users_app.models import UserProfile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users_app.models import Department

# class Userform(UserCreationForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

#     class Meta:
#         model=User
#         fields = ['email','password','phone_number','department']
#         widgets={
#             "email":forms.EmailInput(attrs={"class":"form-control"}),
#             "phone_number":forms.TextInput(attrs={"class":"form-control"}),
#             "department":forms.TextInput(attrs={"class":"form-control"}),
            
#         }




class Userform(ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['email','password','phone_number','department']
        widgets = {'password': forms.PasswordInput()}
        # fields='__all__'

class Deptform(ModelForm):
    class Meta:
        model = Department
        fields=['name','desc']
       

