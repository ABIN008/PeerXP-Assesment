from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from users_app.models import Ticket
from django.urls import reverse_lazy
from users_app.decorators import owner_permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.mail import send_mail
from .forms import Userform,Deptform
from users_app.models import Department


def index(request):
    return render(request, "adminhome.html")


def list_ticket(request):
    objects = Ticket.objects.all()
    return render(request,'ticketlist.html', {'objects': objects})


def Adduser(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
    else:
        form = Userform()
    return render(request, 'adduser.html', {'form': form})


def Adddepartment(request):
    if request.method == 'POST':
        form = Deptform(request.POST,request.FILES)
        if form.is_valid():
            dept = form.save(commit=False)
            dept.user = request.user
            form.save()
    else:
        form = Deptform()
    return render(request, 'add_dept.html', {'form': form})



def list_dept(request):
    objects = Department.objects.all()
    return render(request,'dept_list.html', {'objects': objects})



def update_dept(request,id):
    objects=Department.objects.get(pk=id)
    form= Deptform(request.POST or None,instance=objects)
    if request.method=='POST':
        form= Deptform(request.POST,request.FILES or None,instance=objects)
        if form.is_valid():
            form.save()
            return redirect('dept_list')
    context={'form':form}
    return render(request, 'update_dept.html',context)  



def delete_dept(request,id):
   if request.method=='POST':
    items=Department.objects.filter(pk=id)
    items.delete()
    return redirect('dept_list')


def delete_ticket(request,id):
   if request.method=='POST':
    items=Ticket.objects.filter(pk=id)
    items.delete()
    return redirect('listticket')
