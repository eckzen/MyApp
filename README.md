# MyApp

Django Web App

\$ django-admin startproject mysite

\$ python manage.py runserver

\$ python manage.py startapp polls

First View

- polls/views.py

from django.http import HttpResponse

def index(request):
return HttpResponse("Hello, world. You're at the polls index")

- polls/urls.py

from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
]

- mysite/urls.py

from django.urls import path,include

urlpatterns = [
path('admin/', admin.site.urls),
path('polls/', include('polls.urls')),
]
