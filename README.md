# MyApp
02_models

- pols/models.py

from django.db import models

class Question(models.Model):

    question_text = models.Charfield(max_length=200)
    
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    choice_text = models.CharField(max_length=200)
    
    votes = models.IntegerField(default=0)
    
- myapp/settings.py

INSTALLED_APPS = [

    'polls.apps.PollsConfig',
]

