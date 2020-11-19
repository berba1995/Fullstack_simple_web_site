# Create your views here.
from django.shortcuts import render
from formulaire.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User









def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpRespose("Vous êtes connectés !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo_profil' in request.FILES:
                print('found it')
                profile.photo_profil = request.FILES['photo_profil']
            else:
                profile.photo_profil= "None"

            profile.save()
            registered = True
            login(request,user)

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    if registered:
        return render(request,'index.html',
                              {'user_form':user_form,
                               'profile_form':profile_form,
                               'registered':registered
                               })
    else:
        return render(request,'registration.html',
                              {'user_form':user_form,
                               'profile_form':profile_form,
                               'registered':registered})





def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Votre compte est inactif")
        else:
            return HttpResponse("Nom d'utilisateur et mot de passe invalides")
    else:
        return render(request, 'login.html', {})




def update_user(request):
    if request.method == "POST":
        new_email=request.POST.get('email', False)

        if new_email:
             update_user=request.user

             update_user.email=new_email

             update_user.save()

    return HttpResponse('')
