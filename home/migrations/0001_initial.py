# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='bike_images')),
                ('description', models.TextField()),
                ('daily_rent', models.IntegerField()),
                ('is_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone_number', models.TextField()),
                ('booking_start_date', models.DateField()),
                ('booking_end_date', models.DateField()),
                ('booking_message', models.TextField()),
                ('is_approved', models.BooleanField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Bike')),
            ],
        ),
    ]
