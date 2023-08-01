from django.db import models

# Create your models here.


class Students(models.Model):
    stu_name = models.CharField(max_length=100, default='', verbose_name="Student name")
    stu_roll = models.IntegerField(verbose_name="Roll No.")
    stu_class = models.IntegerField(verbose_name="Class")

    class Meta:
        verbose_name = "Student Detail"

