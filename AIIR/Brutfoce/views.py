from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .forms import LoginForm, UserRegistrationForm, TestForm
from django.contrib.auth.decorators import login_required
from models import Task

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from tasks import handle_task
from celery.result import AsyncResult
import json

import hashlib


def poll_state(request):
    """ A view to report the progress to the user """
    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            task = AsyncResult(task_id)
            data = task.result or task.state
        else:
            data = 'No task_id in the request'
    else:
        data = 'This is not an ajax request'

    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')


def task(request):
    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        state = job.state
        password = job.result
        context = {
            'state': state,
            'password': password,
            'task_id': job_id,
        }

        return render(request, "Brutforce/show_t.html", context)
    elif 'task_id' in request.GET:
        task_id = request.GET['task_id']
        task = Task.objects.get(pk=int(task_id))
        job = handle_task.delay(task.hash, task.dictionary, task.max_password_len, task_id)
        return HttpResponseRedirect(reverse('task') + '?job=' + job.id)
    else:
        return redirect('profile')
    return render(request, "Brutforce/post_task.html", context)


def login(request):
    return render(request, "Brutforce/login.html")


def task_added(request):
    return render(request, "Brutforce/task_added.html")


@login_required
def profile(request):
    queryset = Task.objects.all().filter(author=request.user)
    context = {
        "queryset": queryset
    }
    if request.POST:
        for key, value in request.POST.iteritems():
            if value == 'Start task':
                return HttpResponseRedirect(reverse('task') + '?task_id=' + key)

    return render(request, "Brutforce/profil.html", context)


@login_required
def index(request):
    return render(request, "Brutforce/index.html")


@login_required
def history(request):
    return render(request, "Brutforce/history.html")


@login_required
def tasks(request):
    title = "Here you can add new Task:"
    form = TestForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        md5h = hashlib.md5()
        md5h.update(form.cleaned_data['input_password'].encode('utf-8'))
        instance.hash = md5h.hexdigest()
        instance.save()
        return redirect('task_added')

    return render(request, "Brutforce/tasks.html", context)


def register(request):
    """View for user registration."""
    if request.POST:
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
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

