# Generated by Django 4.1.4 on 2023-01-05 15:35

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):

    dependencies = [
        ("transformers", "0010_remove_transformer_slug_alter_transformer_name"),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AddIndex(
            model_name="transformer",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name", "toyline", "subline", "size_class"],
                name="NewGinIndex",
                opclasses=[
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                ],
            ),
        ),
    ]
