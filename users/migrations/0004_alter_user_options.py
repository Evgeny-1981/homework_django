# Generated by Django 4.2 on 2024-06-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("email",),
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
    ]
