# Generated by Django 4.1.4 on 2023-01-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transformers", "0006_toyline_subline_transformer_subline_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subline",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="toyline",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
