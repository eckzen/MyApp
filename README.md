# MyApp
08_raise404

- polls/views.py

from django.shortcuts import render

from django.http import HttpResponse, Http404

from .models import Question


    def index(request, question_id):
    
        try:
        
            question = Question.objects.get(pk=question_id)
            
        except Question.DoesNotExist:
        
            raise Http404("Question does not exist")
            
        return render(request, 'polls/index.html', {'question': question})


    def detail(request, question_id):
    
        return HttpResponse("You're looking at question %s." % question_id)


    def results(request, question_id):
    
        response = "You're looking at the results ofquestion %s."
        
        return HttpResponse(response % question_id)


    def vote(request, question_id):
    
        return HttpResponse("You're voting on a question %s" % question_id)
        
- polls/templates/polls/index.html

    {% if latest_question_list %}
    
    <ul>
    
      {% for question in latest_question_list %}
      
          <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
          
      {% endfor %}
      
    </ul>
    
    {% else %}
    
        <p>No polls are available</p>
        
    {% endif %}



