from django.shortcuts import render
from django.http import HttpResponse
from elder_gurder_service.forms import UserAdminCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render(request,'index.html')
def registration(request):
    user = UserAdminCreationForm()
    return render(request,'register.html' , context={'form': user})
def people_list(request):
    return render(request,'people_list.html')
def people_detail(request):
    return render(request,'people_detail.html')
def add_visit(request):
    return render(request,'add_visit.html')
def add_visit_permission(request):
    return render(request,'add_visit_permission.html')
def visit_detail(request):
    return render(request,'visit_detail.html')
def edit_visit(request):
    return render(request,'edit_visit.html')
def delete_visit(request):
    return render(request,'delete_visit.html')
def second_user(request):
    return render(request,'second_user.html')
def conectes_list(request):
    return render(request,'conectes_list.html')

