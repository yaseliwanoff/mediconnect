from django.contrib import admin
from .models import Doctor, SpecializationCategory, Patient, Appointment, AppointmentTime

admin.site.register(Doctor)
admin.site.register(SpecializationCategory)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(AppointmentTime)
