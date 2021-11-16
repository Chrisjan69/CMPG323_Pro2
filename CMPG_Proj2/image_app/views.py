from django.shortcuts import render
from image_app.forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, HttpResponseForbidden, QueryDict, HttpResponseNotFound
# Create your views here.

def index(request):
    return render(request,'image_app/index.html')

# def users(request):
#     form = NewUserForm()
#
#     if request.method =='POST':
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit = True)
#             return index(request)
#         else:
#             print('ERROR, FORM INVALID')
#     return render(request,'image_app/users.html',{'form':form})

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


def test(request):
    my_dict =  {'insert_me':'Hello, now i am coming from image_app/index.html!!'}
    return render(request,'image_app/test.html', context = my_dict)
