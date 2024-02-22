from django.contrib.auth.models import User
from django.db import models


class SpecializationCategory(models.Model):
    specialization_title = models.CharField(verbose_name='Specialization title')

    def __str__(self):
        return self.specialization_title


class AppointmentTime(models.Model):
    appointment_time = models.CharField(verbose_name='Available time')

    def __str__(self):
        return self.appointment_time


class Doctor(models.Model):
    photo = models.ImageField(verbose_name='Photo')
    first_name = models.CharField(verbose_name='First name', max_length=80)
    last_name = models.CharField(verbose_name='Last name', max_length=80)
    specialization = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE, related_name='doctors')
    about = models.TextField(blank=True, verbose_name='Information about doctor', max_length=600)
    experience = models.TextField(blank=True, verbose_name='Experience')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_datetime = models.ForeignKey(AppointmentTime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_datetime}"


class Callback(models.Model):
    name = models.CharField(default=None, verbose_name='User callback name')
    email = models.EmailField(default=None, verbose_name='User callback email')
    phone = models.CharField(default=None, max_length=20)
    date = models.DateField(default=None)

    def __str__(self):
        return f"Callback to {self.name}"

