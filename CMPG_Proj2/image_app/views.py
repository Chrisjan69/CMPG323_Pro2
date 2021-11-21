from django.shortcuts import render
from image_app.forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, HttpResponseForbidden, QueryDict, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required #if viwe requires uers to be loged in
from django.views.generic import View

# Create your views here.

def index(request):
    return render(request,'image_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def search_site(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        Album_title = Album.objects.filter(Album_name__contains=searched)
        User_name = User.objects.filter(user_contains)
        return render(request, 'image_app/search_site.html', {'searched':searched, 'albums':album, 'username':username})
    else:
        return render(request, 'image_app/search_site.html', {})



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
