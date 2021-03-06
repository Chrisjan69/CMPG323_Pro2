# Generated by Django 3.2.5 on 2021-11-21 09:53

import django.core.files.storage
from django.db import migrations, models
import image_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0006_image_date_uploaded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/my_sell/', location='/Users/chrisjanrebel/Documents/GitHub/CMPG323_Pro2/CMPG_Proj2/media/my_sell/'), upload_to=image_app.models.image_directory_path)),
            ],
        ),
    ]
