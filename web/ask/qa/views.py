from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from qa.models import Question


def test(request, *args, **kwargs):
    resp = 'OK'
    for par in args:
        resp = resp + ', ' + par
    return HttpResponse(resp)


@require_GET
def question(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    return render(request, 'qa/question.html',
                  {'question': q,
                   'answers': q.answer_set.all()})


@require_GET
def index(request, *args, **kwargs):
    questions = Question.objects.all()
    num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 2)
    paginator = Paginator(questions, limit)
    if len(paginator.page_range) < int(num) or int(num) < 1:
        raise Http404()
    paginator.baseurl = '/?page='
    page = paginator.page(num)
    return render(request, 'qa/page.html',
                  {'posts': page.object_list,
                   'paginator': paginator,
                   'page': page,
                   'question_url': '/question/'})


@require_GET
def popular(request, *args, **kwargs):  # TODO
    resp = 'TODO: show popular here'
    return HttpResponse(resp)