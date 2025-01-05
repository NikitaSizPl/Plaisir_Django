# Generated by Django 5.1.4 on 2025-01-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_item_categories_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catigories',
            name='image_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='catigories',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Изображение'),
        ),
    ]
