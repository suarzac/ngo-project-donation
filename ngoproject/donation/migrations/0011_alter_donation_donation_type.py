# Generated by Django 3.2.4 on 2021-06-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0010_auto_20210628_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(default='', max_length=255, verbose_name='type'),
        ),
    ]
