# Generated by Django 5.2 on 2025-04-25 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0007_remove_property_image_propertyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalApp.category'),
        ),
        migrations.AlterField(
            model_name='property',
            name='disc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='perportyType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalApp.perportytype'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]
