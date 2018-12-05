from django.shortcuts import render
from .models import Question
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'one/index.html', context)

def detail(request,question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'one/detail.html', {'question': question})

def results():
    pass

def vote():
    pass
# Create your views here.
