# MyApp
06_template

- polls/views.py

from django.http import HttpResponse

from django.template import loader

from .models import Question

    def index(request):
    
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        
        template = loader.get_template('polls/index.html')
        
        context = {
        
            'latest_question_list': latest_question_list,
            
        }
        
        return HttpResponse(template.render(context, request))


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



