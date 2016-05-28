"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from schedule.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
	url(r'^$', login),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^password/$', password),
    url(r'^register/$', register),
    url(r'^index/$', login),
    url(r'^logout/$', logout),
    url(r'^main/$', main),
    url(r'^search/$', search),
    #url(r'^login/$', login),
    #url(r'^accounts/', include('users.urls')),
]

urlpatterns += staticfiles_urlpatterns();
