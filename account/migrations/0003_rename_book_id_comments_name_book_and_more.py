# Generated by Django 5.0.3 on 2024-04-03 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_book_comments_book_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='book_id',
            new_name='name_book',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='user_id',
            new_name='user_creator',
        ),
    ]
