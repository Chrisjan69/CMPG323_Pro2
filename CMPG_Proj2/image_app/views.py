from django.shortcuts import render
from image_app.register import NewUserForm
# Create your views here.

def index(request):
    return render(request,'image_app/index.html')

def register(request):
    form = NewUserForm
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('ERROR, PLEASE CHECK ALL FIELDS')
    return render(request, 'image_app/register.html',{'form':form})



def test(request):
    my_dict =  {'insert_me':'Hello, now i am coming from image_app/index.html!!'}
    return render(request,'image_app/test.html', context = my_dict)
