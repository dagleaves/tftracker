# Generated by Django 4.1.5 on 2023-02-09 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="avatar",
            field=models.ImageField(default=None, null=True, upload_to="avatars"),
        ),
    ]
