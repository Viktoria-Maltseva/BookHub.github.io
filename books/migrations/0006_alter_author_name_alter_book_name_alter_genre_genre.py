# Generated by Django 5.0.3 on 2024-04-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_genre_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=255),
        ),
    ]