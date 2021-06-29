# Generated by Django 3.2.4 on 2021-06-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_remove_donation_donation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='recurring',
            field=models.BooleanField(default=False),
        ),
    ]
