from django.shortcuts import HttpResponse
import datetime


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        data = datetime.datetime.now().date()
        return HttpResponse(f'Data: {data}')


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user')
