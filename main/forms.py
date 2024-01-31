from django import forms
from .models import AppointmentTime, Appointment, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'reg-user'}))
    phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))


class AppointmentForm(forms.ModelForm):
    appointment_datetime = forms.ModelChoiceField(queryset=AppointmentTime.objects.all(), empty_label='Select your appointment time')

    class Meta:
        model = Appointment
        fields = ['appointment_datetime', 'doctor', 'user']

    def __str__(self):
        return str(self.appointment_datetime)
