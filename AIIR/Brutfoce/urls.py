from django.conf.urls import url, include
from . import views


urlpatterns = (
#login/logout
    url('^', include('django.contrib.auth.urls')),
###
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profil/$', views.get_info, name='profil'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^history/$', views.history, name='history'),
    url(r'^register/$', views.register, name='register'),
)