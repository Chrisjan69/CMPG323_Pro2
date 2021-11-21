from django.shortcuts import render
from image_app.forms import NewUserForm,ImageForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, HttpResponseForbidden, QueryDict, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required #if viwe requires uers to be loged in
from django.views.generic import View, TemplateView, DetailView, ListView
from image_app import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit  import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'image_app/index.html')

def view_picture(request):
    # c = models.UserImage.objects.order_by('-date_uploaded')
    # imgform = ImageForm()
    # return render (request,'image_app/Display_Images_detail.html', {'userImage' :c, 'imgform' :imgform})

    c = dict()
    c['userimage'] = models.UserImage.objects.all().order_by('-date_uploaded')
    imgform = ImageForm()
    return render(request,'image_app/Display_Images_detail.html',c)




class ImageCreateView(LoginRequiredMixin,CreateView):
    fields = ('title','desc','location','date_uploaded','pic','album_name')
    model = models.UserImage
    template_name = 'image_app/userimage_form.html'

class ImageUpdateView(LoginRequiredMixin,UpdateView):
    fields = ('title','desc','location','date_uploaded','album_name')
    model = models.UserImage


class ImageDeleteView(DeleteView):
   model = models.UserImage
   success_url=reverse_lazy('image_app:images')

class AlbumDisplayView(LoginRequiredMixin,ListView):
    model = models.Album
    template_name = 'image_app/Display_Albums_detail.html'
    context_object_name = 'album_display'


# class ImageDisplayView(LoginRequiredMixin,ListView):
#     model = models.Image
#     template_name = 'image_app/Display_Images_detail.html'
#     context_object_name = 'image_display'


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def search_site(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        image_title = models.UserImage.objects.filter(title__contains=searched)
        # username = models.User.objects.filter(user__contains = searched)
        return render(request, 'image_app/image_searched.html', {'searched':searched, 'image_title':image_title,})
    else:
        return render(request, 'image_app/image_searched.html', {})



def users(request):
    registered = False

    if request.method == "POST":

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = NewUserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Registration Successful!
            registered = True
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = NewUserForm()
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'image_app/users.html',
                {'user_from':user_form,
                'registered':registered})


def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password) #authenticates User

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Found, Please register an account")
        else:
            print("A person without an account tried loggin in")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("Invalid login details supplied, Please check username and password or create an Account")
    else:
        return render(request, "image_app/login.html",{})



def test(request):
    my_dict =  {'insert_me':'Hello, now i am coming from image_app/index.html!!'}
    return render(request,'image_app/test.html', context = my_dict)
