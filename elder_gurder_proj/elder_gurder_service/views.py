from django.shortcuts import render
from django.http import HttpResponse
from elder_gurder_service.forms import UserAdminCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homepage(request):
    return render(request,'index.html')
def registration(request):
    
    if request.method == 'POST':
        form_user = UserAdminCreationForm(request.POST)
        if form_user.is_valid():
            #create the user
            form_user.save()
            # getting details
            username     = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            
            print(username , raw_password)
            # authenticate user
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('people_list')
            else:
                return redirect('register')
    else:
        form_user = UserAdminCreationForm()
        return render(request,'register.html' , context={'form': form_user})
    
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

