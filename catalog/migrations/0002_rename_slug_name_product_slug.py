# Generated by Django 4.2 on 2024-06-27 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="slug_name",
            new_name="slug",
        ),
    ]
