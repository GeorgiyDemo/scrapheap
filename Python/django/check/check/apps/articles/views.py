from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")


# Create your views here.
def test(request):
    return HttpResponse("TEST")


class OrderView():
    pass
