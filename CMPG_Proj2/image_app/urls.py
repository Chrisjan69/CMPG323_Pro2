from django.conf.urls import url
from image_app import views
from django.urls import path


urlpatterns = [

    path('',views.users,name='users'),

]
 
