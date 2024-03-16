from django.contrib import admin
from .models import Doctor, SpecializationCategory, Appointment, Callback, AppointmentTime

admin.site.register(Doctor)
admin.site.register(SpecializationCategory)
admin.site.register(Appointment)
admin.site.register(AppointmentTime)
admin.site.register(Callback)


