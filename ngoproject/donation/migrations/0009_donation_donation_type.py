# Generated by Django 3.2.4 on 2021-06-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0008_auto_20210628_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(default='', max_length=255),
        ),
    ]
