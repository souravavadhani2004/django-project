from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    Age = models.IntegerField(default=20)
    Phonenumber = models.IntegerField(default=983489237498)
    def __str__(self):
        return self.name
    # models.py

from django.db import models

class GymMember(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Basic information
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name