from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse




class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def _str_(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Album(models.Model):
    album_name = models.CharField(max_length = 200, unique = True)
    user_name = models.ForeignKey(User,related_name ='u_album_name', on_delete = models.CASCADE)
    date_created = models.DateField()

    def __str__(self):
        return str(self.album_name)

# class Image(models.Model):
#     title = models.CharField(max_length = 15, unique = True)
#     desc = models.CharField(max_length = 300, unique = True)
#     location = models.CharField(max_length = 30, unique = True)
#     album_name = models.ForeignKey(Album,related_name='image_in_album', on_delete = models.CASCADE)
#     image = models.ImageField(blank = True, null = True)
#     date_uploaded = models.DateField(blank = True, null = True)


    # def __str__(self):
    #     return self.title


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)


class UserImage(models.Model):

    pic = models.ImageField(upload_to=image_directory_path, storage=image_storage)
    title = models.CharField(max_length = 200, unique = True)
    desc = models.CharField(max_length = 300, unique = True)
    location = models.CharField(max_length = 30, unique = False)
    album_name = models.ForeignKey(Album,related_name='image_in_album', on_delete = models.CASCADE)
    date_uploaded = models.DateField(blank = True, null = True)
    class Meta:
        ordering = ('date_uploaded',)
    def get_absolute_url(self):
        return reverse('image_app:images')

    def __str__(self):
        return self.title








# Create your models here.
