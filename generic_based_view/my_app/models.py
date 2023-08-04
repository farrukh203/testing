from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
]


class Students(models.Model):
    """
    Create a Students model
    and course have ManytoMany relation with course model
    """
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length=20, choices=GENDER)
    address = models.CharField(max_length=100)

    standard = models.IntegerField()
    course = models.ManyToManyField("Course", blank=True)

    father_name = models.CharField(max_length=100)
    parent_contact_number = models.BigIntegerField()

    profile_image = models.ImageField(upload_to='my_app/media/profile/', blank=True)
    stu_created_at = models.DateTimeField(default=datetime.datetime.now())
    stu_updated_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = "Student Detail"
        verbose_name_plural = "Student Details"
        ordering = ("last_name", "first_name")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def save(self, *args, **kwargs):
        self.stu_updated_at = datetime.datetime.now()
        super(Students, self).save(*args, **kwargs)


class Course(models.Model):
    """
    Create a Course model with field name, year
    """
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year")

    def __str__(self):
        return f"{self.name}, {self.year}"


class Grade(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, default='')
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.grade}, {self.student}, {self.course}"
