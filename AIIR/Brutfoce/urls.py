from django.conf.urls import url, include
from . import views


urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^history/$', views.history, name='history'),
    url(r'^register/$', views.register, name='register'),
    #login/logout
    url('^', include('django.contrib.auth.urls')),
)