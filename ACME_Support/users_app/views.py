from email import message
from urllib.request import Request
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import View,ListView
import requests
from users_app.decorators import sign_in_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import View
from django.views.generic import View,ListView
from ACME_Support.settings import ZENDESK_API_TOKEN
from .models import Ticket
from .forms import TicketForm,LoginForm

# Create your views here.



class SignInView(View):
    def get(self,request):
        form=LoginForm()
        context={"form":form}
        return render(request,"signin.html",context)
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect('admin_index')
                elif request.user==user:
                    return redirect('user_index')
                    # return render(request,'userhome.html')
                else:
                    return redirect("signin")
            else:
                context={"form":form}
                return render(request,"signin.html",context)

def user_index(request):
    return render(request, "userhome.html")


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            
            # post ticket to Zendesk API
            headers = {'Content-Type': 'application/json'}
            data = {
                'subject': ticket.subject,
                'description': ticket.description
            }
            requests.post('https://abin3698.zendesk.com/api/v2/tickets.json', headers=headers, data=data)

            return redirect('tickets')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})




@login_required
def tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets.html', {'tickets': tickets})



class MyticketView(ListView):
    model= Ticket
    context_object_name = "items"
    template_name = "tickets.html"
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)



