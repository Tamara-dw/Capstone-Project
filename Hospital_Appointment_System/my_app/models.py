from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Dr. {self.full_name} - {self.specialization}"


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='appointments')
    appointment_datetime = models.DateTimeField()  
    description = models.TextField(blank=True)

    def __str__(self):
       return f"{self.appointment_datetime} - {self.patient.username if self.patient else 'No Patient'} with Dr. {self.doctor.full_name}"

