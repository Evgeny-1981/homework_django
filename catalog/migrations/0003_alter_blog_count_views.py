# Generated by Django 5.0.4 on 2024-05-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blog_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='count_views',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='счетчик просмотров'),
        ),
    ]
