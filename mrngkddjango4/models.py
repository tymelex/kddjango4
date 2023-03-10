from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(default='Kenya', max_length=100)
    city = models.CharField(default='Nairobi', max_length=100)
    amount = models.IntegerField(blank=False, null=False)
def __str__(self):
    return self.name

