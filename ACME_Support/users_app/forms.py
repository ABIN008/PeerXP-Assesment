from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields=['subject','description']
        
class LoginForm(forms.Form): 
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())