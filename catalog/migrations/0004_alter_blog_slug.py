# Generated by Django 4.2 on 2024-06-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.CharField(max_length=120, unique=True, verbose_name="слаг"),
        ),
    ]
