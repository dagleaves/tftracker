# Generated by Django 4.1.4 on 2023-01-01 19:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transformers", "0002_transformer_picture"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transformer", options={"ordering": ("-name",)},
        ),
        migrations.AddField(
            model_name="transformer",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, null=True, populate_from="name", unique=True
            ),
        ),
    ]
