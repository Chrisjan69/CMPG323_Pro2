from django.conf.urls import url
from image_app import views
from django.urls import path

#template tagging
app_name = 'image_app'

urlpatterns = [


    path('register/',views.users,name='users'),
    path('login/',views.user_login, name = 'user_login'),
    path('logout/',views.user_logout,name='user_logout'),



]
