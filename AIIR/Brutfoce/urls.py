from django.conf.urls import url, include
from . import views


urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^$', views.charts, name='charts'),
    url(r'^register/$', views.register, name='register'),
    #login/logout
    url('^', include('django.contrib.auth.urls')),
)