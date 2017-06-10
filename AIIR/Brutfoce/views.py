from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "Brutforce/index.html")


def charts(request):
    return render(request, "Brutforce/charts.html")

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Sukces!!!')
                else:
                    return HttpResponse('Wylaczony')
            else:
                return HttpResponse('Zly login i haslo')
    else:
        form = LoginForm()
    return render(request, 'Brutforce/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            #Tworzenie nowego obiektu User bez zapisywania go
            new_user = user_form.save(commit=False)
            #Ustawienie wybranego hasla
            new_user.set_password(user_form.cleaned_data['password'])
            #Zapisanie obiektu User
            new_user.save()
            return render(request,
                          'Brutforce/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'Brutforce/register.html', {'user_form': user_form})
