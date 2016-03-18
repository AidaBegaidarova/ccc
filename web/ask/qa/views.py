from django.shortcuts import render

from django.http import HttpResponse 
def test(request, *args, **kwargs):
    resp = 'OK'
    for par in args:
        resp = resp + ', ' + par
    return HttpResponse(resp)
