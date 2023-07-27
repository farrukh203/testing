from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    address = models.CharField(max_length=100)

    standard = models.IntegerField()
    course = models.ManyToManyField("Course", blank=True)

    father_name = models.CharField(max_length=100)
    parent_contact_number = models.BigIntegerField()

    profile_image = models.ImageField(upload_to='media/profile/', blank=True)

    class Meta:
        verbose_name = "Student Detail"
        verbose_name_plural = "Student Details"
        #ordering = ("last_name", "first_name")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


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
