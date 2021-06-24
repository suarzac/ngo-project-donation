# Generated by Django 3.2.4 on 2021-06-24 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(default='', max_length=200)),
                ('last_name', models.TextField(default='', max_length=200)),
                ('cell_num', models.CharField(default='', max_length=14)),
                ('phone_num', models.CharField(default='', max_length=14)),
                ('usr_email', models.EmailField(default='', max_length=200)),
                ('usr_addr1', models.CharField(max_length=50)),
                ('usr_addr2', models.CharField(max_length=50)),
                ('usr_city', models.TextField(default='', max_length=50)),
                ('usr_state', models.TextField(default='', max_length=50)),
                ('usr_zip', models.IntegerField(default='')),
                ('usr_country', models.TextField(default='', max_length=50)),
                ('urbanization', models.TextField(default='', max_length=50)),
                ('donation_amount', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(default='', max_length=200)),
                ('last_name', models.TextField(default='', max_length=200)),
                ('usr_email', models.EmailField(default='', max_length=200)),
                ('usr_password', models.CharField(max_length=200)),
                ('role_opt', models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='User', max_length=5)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
