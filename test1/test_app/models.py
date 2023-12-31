import datetime

from django.db import models

# Create your models here.


# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     age = models.PositiveIntegerField(default=15)
#
#     class Meta:
#         abstract = True
#
#
# class Student(CommonInfo):
#     group = models.CharField(max_length=100, default='model_group')
#
#     def __str__(self):
#         return f"{self.name} {self.age}"


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.address}"

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Supplier(Place):
    place_id = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        parent_link=True, primary_key=True
    )
    customers = models.ManyToManyField(
        Place,
        related_name="%(app_label)s_%(class)s_related"
    )


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return f'{self.group_name}'


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.date_joined}'
