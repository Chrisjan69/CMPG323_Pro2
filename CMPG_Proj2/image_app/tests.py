from django.test import TestCase
from django.db import models


# Create your tests here.

class URLTest(TestCase):
    def test_testIndexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class Album(models.Model):
    album_name = models.CharField(max_length = 200, unique = True)
    user_name = models.ForeignKey(User,related_name ='u_album_name', on_delete = models.CASCADE)
    date_created = models.DateField()

    def __str__(self):
        return str(self.album_name)


class UserImage(models.Model):

    pic = models.ImageField(upload_to=image_directory_path, storage=image_storage)
    title = models.CharField(max_length = 15, unique = True)
    desc = models.CharField(max_length = 300, unique = True)
    location = models.CharField(max_length = 30, unique = False)
    album_name = models.ForeignKey(Album,related_name='image_in_album', on_delete = models.CASCADE)
    date_uploaded = models.DateField(blank = True, null = True)
    class Meta:
        ordering = ('date_uploaded',)
    def get_absolute_url(self):
        return reverse('image_app:images', )

    def __str__(self):
        return self.title
