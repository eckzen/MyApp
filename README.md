# MyApp
05_webpages

- polls/views.py

from django.http import HttpResponse


    def index(request):
    
        return HttpResponse("Hello, world. You're at the polls index")


    def detail(request, question_id):
    
        return HttpResponse("You're looking at question %s." % question_id)


    def results(request, question_id):
    
        response = "You're looking at the results ofquestion %s."
        
        return HttpResponse(response % question_id)


    def vote(request, question_id):
    
        return HttpResponse("You're voting on a question %s" % question_id)
        
        
- polls/urls.py

from django.urls import path

from . import views

    urlpatterns = [
    
        path('', views.index, name='index'),
        
        path('<int:question_id>/', views.detail, name='detail'),
        
        path('<int:question_id>/results/', views.results, name='results'),
        
        path('<int:question_id>/vote/', views.vote, name='vote'),
        
    ]

