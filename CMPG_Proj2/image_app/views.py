from django.shortcuts import render
from django.http import HttpResponse
from image_app.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'acces_records': webpages_list}

    return render(request,'image_app/index.html', context = date_dict)

def test(request):
    my_dict =  {'insert_me':'Hello, now i am coming from image_app/index.html!!'}
    return render(request,'image_app/test.html', context = my_dict)
