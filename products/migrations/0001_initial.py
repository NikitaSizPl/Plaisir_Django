# Generated by Django 5.1.4 on 2025-01-30 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catigories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('image_id', models.IntegerField(blank=True, null=True, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('image_id', models.IntegerField(blank=True, null=True, verbose_name='Изображение')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.catigories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
