from django.contrib import admin
from image_app.models import Album,UserProfileInfo,UserImage


# Register your models here.
admin.site.register(UserProfileInfo)
# admin.site.register(Image)
admin.site.register(Album)
admin.site.register(UserImage)
