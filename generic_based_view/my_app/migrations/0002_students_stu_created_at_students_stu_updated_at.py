# Generated by Django 4.2.3 on 2023-08-03 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='stu_created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='stu_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
