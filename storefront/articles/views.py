from django.shortcuts import render
from .models import Article 
from django.http import HttpResponse
# Create your views here.

def index(request):
    articles=Article.objects.all().order_by('date')
    return render(request,"index.html",{'articles':articles})


def article_detail(request,slug):
    #return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,"article_detail.html",{'article':article})