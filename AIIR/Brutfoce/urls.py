from django.conf.urls import url, include
from . import views


urlpatterns = (
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    #login/logout
    url('^', include('django.contrib.auth.urls')),
)