from django.conf.urls import url, include
from . import views


urlpatterns = (
#login/logout
    url('^', include('django.contrib.auth.urls')),
###
    url(r'^$', views.index, name='index'),
    url(r'^task/$', views.task, name='task'),
    url(r'^task/poll_state$', views.poll_state, name='poll_state'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^history/$', views.history, name='history'),
    url(r'^register/$', views.register, name='register'),
    url(r'^task_added/$', views.task_added, name='task_added'),
)