# Generated by Django 4.2.3 on 2023-08-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]