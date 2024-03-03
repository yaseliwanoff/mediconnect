from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class SpecializationCategory(models.Model):
    specialization_title = models.CharField(verbose_name='Specialization title')

    def __str__(self):
        return self.specialization_title


class Doctor(models.Model):
    photo = models.ImageField(verbose_name='Photo')
    first_name = models.CharField(verbose_name='First name', max_length=80)
    last_name = models.CharField(verbose_name='Last name', max_length=80)
    specialization = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE, related_name='doctors')
    about = models.TextField(blank=True, verbose_name='Information about doctor', max_length=600)
    experience = models.TextField(blank=True, verbose_name='Experience')
    visit_price = models.IntegerField(verbose_name='Visit price')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AppointmentTime(models.Model):
    appointment_time = models.CharField(max_length=10, verbose_name='Appointment times', unique=True)

    def __str__(self):
        return f"{self.appointment_time}"


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_day = models.DateField(default=timezone.now)
    appointment_time = models.ForeignKey(AppointmentTime, on_delete=models.CASCADE)
    time_ordered = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.doctor} | day: {self.appointment_day} | time: {self.appointment_time} | visit price: {self.doctor.visit_price} $"


class Callback(models.Model):
    name = models.CharField(default=None, verbose_name='User callback name')
    email = models.EmailField(default=None, verbose_name='User callback email')
    phone = models.CharField(default=None, max_length=20)
    date = models.DateField(default=None)

    def __str__(self):
        return f"Callback to {self.name}"


class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
