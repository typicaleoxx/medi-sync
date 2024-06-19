from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=240)
    email = models.EmailField()
    password = models.CharField(max_length=240)

    ROLE_CHOICES = [
        ("ADMIN", "Administrator"),
        ("DOCTOR", "Doctor"),
        ("NURSE", "Nurse"),
        ("RECEPTIONIST", "Receptionist"),
        ("PATIENT", "Patient"),
        ("MANAGER", "Manager"),
        ("LAB_TECH", "Lab Technician"),
        ("PHARMACIST", "Pharmacist"),
        ("ACCOUNTANT", "Accountant"),
        ("EMERGENCY_STAFF", "Emergency_staff"),
    ]

    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default="PATIENT")

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.first_name
