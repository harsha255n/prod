# Generated by Django 5.0.7 on 2024-08-16 03:25

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ProductImage',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
