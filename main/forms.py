from django import forms
from .models import AppointmentTime, Appointment


class AppointmentForm(forms.ModelForm):
    appointment_datetime = forms.ModelChoiceField(queryset=AppointmentTime.objects.all(), empty_label='Select your appointment time')

    class Meta:
        model = Appointment
        fields = ['appointment_datetime', 'doctor', 'patient']

    def __str__(self):
        return str(self.appointment_datetime)
