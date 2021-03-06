
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/index.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results ofquestion %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on a question %s" % question_id)
