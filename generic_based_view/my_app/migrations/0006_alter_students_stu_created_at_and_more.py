# Generated by Django 4.2.3 on 2023-08-03 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_students_stu_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stu_created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 17, 22, 46, 881676)),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 17, 22, 46, 881676)),
        ),
    ]