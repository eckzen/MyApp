# MyApp

00_view

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

