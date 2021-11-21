from django.conf.urls import url
from image_app import views
from django.urls import path
from django.views.generic import View, TemplateView, DetailView



#template tagging
app_name = 'image_app'

urlpatterns = [


    path('register/',views.users,name='users'),
    path('login/',views.user_login, name = 'user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    # path('images/',views.ImageDisplayView.as_view()),
    path('images/',views.view_picture, name = 'images'),
    path('upload/',views.ImageCreateView.as_view(), name = 'upload'),
    path('update/<pk>',views.ImageUpdateView.as_view(), name = 'update'),
    path('delete/<pk>/',views.ImageDeleteView.as_view(),name='delete'),
    path('search_site',views.search_site, name='search_site'),






]
