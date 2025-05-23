# Generated by Django 5.2 on 2025-04-25 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0005_rename_category2_perportytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=200)),
                ('disc', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentalApp.category')),
                ('perportyType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentalApp.perportytype')),
            ],
        ),
    ]
