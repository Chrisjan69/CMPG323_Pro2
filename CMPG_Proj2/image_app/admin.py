from django.contrib import admin



from image_app.models import Image,Album,UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Image)
admin.site.register(Album)
