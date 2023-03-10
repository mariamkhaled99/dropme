# Generated by Django 4.1.7 on 2023-02-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0003_usermodel_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='gender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='profile_photo',
            field=models.ImageField(default='users_api/default.jpg', upload_to='upload_to'),
        ),
    ]