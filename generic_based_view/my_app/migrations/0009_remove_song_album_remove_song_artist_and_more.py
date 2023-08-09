# Generated by Django 4.2.3 on 2023-08-08 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_album_artist_alter_students_stu_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 8, 16, 35, 47, 880100)),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 8, 16, 35, 47, 880100)),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
