# Generated by Django 4.1.4 on 2023-01-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transformers", "0009_add_pg_trgm_extension"),
    ]

    operations = [
        migrations.RemoveField(model_name="transformer", name="slug",),
        migrations.AlterField(
            model_name="transformer",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
