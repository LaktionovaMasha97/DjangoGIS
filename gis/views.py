from django.http import HttpResponse
from django.shortcuts import render

from gis.models import Articleas


def home(request):
    # return HttpResponse("Hello world")
    # return render(request, 'gis/home.html')
    articles = Articleas.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'gis/home.html', context)


def about(request):
    return render(request, 'gis/about.html')