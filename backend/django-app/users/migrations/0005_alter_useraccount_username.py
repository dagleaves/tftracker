# Generated by Django 4.1.5 on 2023-03-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_useraccount_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useraccount",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]