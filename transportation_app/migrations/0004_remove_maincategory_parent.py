# Generated by Django 4.0 on 2021-12-15 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation_app', '0003_maincategory_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maincategory',
            name='parent',
        ),
    ]
