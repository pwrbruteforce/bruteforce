from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login


from .forms import LoginForm, UserRegistrationForm, TestForm
from django.contrib.auth.decorators import login_required
from models import Task
import sys
import subprocess
from subprocess import Popen, PIPE

def login(request):
    return render(request, "Brutforce/login.html")

@login_required
def get_info(request):
    if request.user.is_authenticated():
        queryset = Task.objects.all().filter(author = request.user)
        context = {
            "queryset": queryset
        }
    return render(request,"Brutforce/profil.html", context)

@login_required
def index(request):
    return render(request, "Brutforce/index.html")

@login_required
def history(request):
    return render(request, "Brutforce/history.html")


def handle_task(hash, dictionary, length):

    password = subprocess.check_output(['python', "C:\\MPI\\brute.py",
                             hash, str(length), str(dictionary)])
 #   stdout, stderr = proc.communicate()
 #   print(password.stdout.read())
    return password


@login_required
def tasks(request):
    title = "Here you can add new Task:"
    form = TestForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        data = request.POST['description']
        hash = form.cleaned_data['hash']
        length = form.cleaned_data['max_password_len']
        dictionary = form.cleaned_data['dictionary']
        password = handle_task(hash, length, dictionary)
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        context = {
            "title": "You just added new task!"
        }
        return render(request, 'Brutforce/tasks.html', {
            'password': password,
            'data': data,
        })
 #   return render_to_response('Brutforce/tasks.html', context=RequestContext(request))
    return render(request, "Brutforce/tasks.html", context)


def show_loaded(request):
    return render_to_response('thanks.html', {'globalok':password}, context_instance=RequestContext(request))

@login_required
def profil(request):
    return render(request, "Brutforce/profil.html")

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

