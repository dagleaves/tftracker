# Generated by Django 4.1.4 on 2023-01-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_useraccount_id_alter_useraccount_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useraccount",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        
    ]
