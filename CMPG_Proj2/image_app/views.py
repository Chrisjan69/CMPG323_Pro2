from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict =  {'insert_me':'Hello, now i am coming from image_app/index.html!!'}
    return render(request,'image_app/index.html', context = my_dict)

def test(request):
    my_dict =  {'insert_me':'Hello, now i am coming from image_app/index.html!!'}
    return render(request,'image_app/test.html', context = my_dict)
