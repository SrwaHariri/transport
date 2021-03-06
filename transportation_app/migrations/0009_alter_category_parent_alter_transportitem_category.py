# Generated by Django 4.0 on 2021-12-16 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation_app', '0008_category_remove_subcategory_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transportation_app.category'),
        ),
        migrations.AlterField(
            model_name='transportitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='item', to='transportation_app.category'),
        ),
    ]
