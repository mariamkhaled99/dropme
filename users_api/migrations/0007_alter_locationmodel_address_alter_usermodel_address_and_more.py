# Generated by Django 4.1.7 on 2023-03-09 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0006_alter_usermodel_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='address',
            field=models.CharField(default='Egypt', max_length=50),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='address',
            field=models.ForeignKey(default='Egypt', null=True, on_delete=django.db.models.deletion.CASCADE, to='users_api.locationmodel'),
        ),
        migrations.CreateModel(
            name='ResetPasswordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_pass_token', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
