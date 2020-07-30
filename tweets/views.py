from django.shortcuts import render
from .models import Tweet
from django.http import JsonResponse
# Create your views here.
import random

def home_view(request,*args,**kwargs):
    template = "pages/home.html"
    context = {}
    return render(request,template,context)


def tweet_list_view(request,*args,**kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id":x.id,"content":x.content,"likes":random.randint(0,100)} for x in qs]
    data = {
        "response":tweet_list,
    }
    return JsonResponse(data)