from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from qa.models import Question


def test(request, *args, **kwargs):
    resp = 'OK'
    for par in args:
        resp = resp + ', ' + par
    return HttpResponse(resp)


def question(request, id):  # TODO
    q = get_object_or_404(Question, id=id)
    return render(request, 'qa/question.html',
                  {'question': q})


def index(request, *args, **kwargs):  # TODO
    resp = 'TODO: show page here'
    return HttpResponse(resp)


def popular(request, *args, **kwargs):  # TODO
    resp = 'TODO: show popular here'
    return HttpResponse(resp)