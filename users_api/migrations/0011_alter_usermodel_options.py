# Generated by Django 4.1.7 on 2023-03-12 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users_api", "0010_remove_usermodel_points_usermodel_total_points"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usermodel",
            options={"ordering": ("-total_points",)},
        ),
    ]
