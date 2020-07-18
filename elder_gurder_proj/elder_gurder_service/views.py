from django.shortcuts import render
from django.http import HttpResponse
from elder_gurder_service.forms import UserAdminCreationForm , UserAuthForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.views.generic import ( ListView, DeleteView, CreateView,
                                 DetailView, TemplateView, UpdateView )
from elder_gurder_service import models

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        print(request.POST)
        # user_login_form = UserAuthForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # print(user_login_form.is_valid())
        # if user_login_form.is_valid():
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('people_list')
        else:
            form_user = UserAdminCreationForm()
            return HttpResponseRedirect('registration',{'form':form_user})

    user_login_form = UserAuthForm()
    return render(request,'index.html' , context={'form': user_login_form})



def registration(request):
    
    if request.method == 'POST':
        form_user = UserAdminCreationForm(request.POST)
        if form_user.is_valid():
            #create the user
            form_user.save()
            # getting details
            email     = form_user.cleaned_data.get('email')
            raw_password1 = form_user.cleaned_data.get('password1')
            raw_password2 = form_user.cleaned_data.get('password2')

            if raw_password1 == raw_password2:
                # authenticate user
                user = authenticate(username=email, password=raw_password1)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('people_list')
                else:
                    form_user = UserAdminCreationForm()
                    return HttpResponseRedirect('registration',{'form':form_user})
            else:
                form_user = UserAdminCreationForm()
                return HttpResponseRedirect('registration',{'form':form_user, 'error': 'password not macth'})

    form_user = UserAdminCreationForm()
    return render(request,'register.html' , context={'form': form_user})


class LonelyPeoples(ListView):
    model = models.LonelyPeople
    context_object_name = 'lonely_peoples'
    template_name = 'people_list.html'

class LonelyDetails(DetailView):
    context_object_name = 'lonely_person'
    model = models.LonelyPeople
    template_name = 'people_detail.html'

class CreateLonely(CreateView):
    model  = models.LonelyPeople
    fields = ["name",'age','address','phone','deatils']
    template_name = 'lonelypeople_form.html'

    def form_valid(self, form):
        print(self.request)
        form.instance.user = self.request.user
        return super(CreateLonely, self).form_valid(form)

@login_required   
def people_list(request):
    return render(request,'people_list.html')

@login_required
def people_detail(request):
    return render(request,'people_detail.html')

@login_required
def add_visit(request):
    return render(request,'add_visit.html')

@login_required
def add_visit_permission(request):
    return render(request,'add_visit_permission.html')

@login_required
def visit_detail(request):
    return render(request,'visit_detail.html')

@login_required
def edit_visit(request):
    return render(request,'edit_visit.html')

@login_required
def delete_visit(request):
    return render(request,'delete_visit.html')

