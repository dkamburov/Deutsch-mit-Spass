from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from website.forms import LoginForm, RegisterForm

def index(request):
    return render(request, 'home.html', locals())


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('welcome')
                else:
                    return redirect('/notlogin')
            else:
                return redirect('/incorrect')
            return HttpResponseRedirect('/thanks/')
    else:
        form = LoginForm()

    return render(request, 'home.html', {
        'form': form,
    })

def welcome(request):
    if request.user.is_anonymous():
        return render(request, 'welcome.html')
    role = request.user.ROLE_CHOISES[request.user.role][1]
    return render(request, 'welcome.html', {
        'username': request.user.username,
        'role': role
    })

def logout_view(request):
    logout(request)
    return redirect('welcome')

def register_view(request):
    data = request.POST if request.POST else None
    form = RegisterForm(data)
    registered = False
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    return render(request, 'register.html', locals())

def exercises_view(request):
    pass
