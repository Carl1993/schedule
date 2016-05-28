from django.conf.urls import url
from schedule import views
 
urlpatterns = [
    url(r'^$', views.login),
    url(r'^password/$', views.password),
    url(r'^register/$', views.register),
    url(r'^index/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^main/$', views.main),
]