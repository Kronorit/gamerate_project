from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from reviews.models import Review
from .forms import UserAuthenticationForm, UserRegistrationForm, UserCreationForm

# Create your views here.

def review_index(request):
    request.session['last_url'] = request.build_absolute_uri()
    reviews = Review.objects.all()
    userId = request.session.get('_auth_user_id')
    if userId == None:
        user = None
    else:
        user = User.objects.get(pk=userId)
    page = request.META.get('HTTP_REFERER')
    return render(request, 'index.html', {'reviews': reviews, 'user':user, 'page': page})

def userLogin(request):
    if request.method == 'POST':
        last_url = request.session['last_url']
        userForm = UserAuthenticationForm(request, request.POST)
        if userForm.is_valid():
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if last_url != None:
                    return redirect(last_url)
                else:
                    return redirect('/')
        else:
            userForm = UserAuthenticationForm()
            return render(request, 'login.html', {'userForm': userForm}) 
    else:
        userForm = UserAuthenticationForm()
        return render(request, 'login.html', {'userForm': userForm})

def userLogout(request):
    logout(request)
    return redirect('/')

'''
MODIFICAR METODO DE VALIDACIÓN DE CONTRASEÑA
'''

def userRegister(request):
    last_url = request.session['last_url']
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('sí')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = User.objects.create_user(username=username, 
                                            password=password, 
                                            email='', 
                                            date_joined=datetime.now())
            user.save()
            login(request, user)
            return redirect(last_url)
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})
