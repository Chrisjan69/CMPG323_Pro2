# Generated by Django 3.2.5 on 2021-11-10 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=200, unique=True)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
                ('desc', models.CharField(max_length=300, unique=True)),
                ('geo_comment', models.CharField(max_length=30, unique=True)),
                ('date_uploaded', models.DateField()),
                ('a_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_in_album', to='image_app.album')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('password', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
        migrations.AddField(
            model_name='album',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_album_name', to='image_app.user'),
        ),
    ]