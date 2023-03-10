# Generated by Django 4.1.5 on 2023-02-02 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("transformers", "0012_alter_transformer_picture"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CollectionItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "priority",
                    models.PositiveIntegerField(
                        choices=[
                            ("1", "Highest"),
                            ("2", "High"),
                            ("3", "Medium"),
                            ("4", "Low"),
                            ("5", "Lowest"),
                        ],
                        default=None,
                        null=True,
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "transformer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transformers.transformer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("public", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
