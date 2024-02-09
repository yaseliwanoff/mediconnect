from django import forms
from .models import AppointmentTime, Appointment, User, SpecializationCategory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import DateInput


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=DateInput(attrs={'class': 'reg-user', 'type': 'date'}))  # Используем DateInput с атрибутом type="date"
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'reg-user'}))
    phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))

    class Meta:
        model = User
        fields = ('username', 'date_of_birth', 'email', 'phone_number', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))


class AppointmentForm(forms.ModelForm):
    appointment_datetime = forms.ModelChoiceField(queryset=AppointmentTime.objects.all(),
                                                  empty_label='Select your appointment time')

    class Meta:
        model = Appointment
        fields = ['appointment_datetime']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


class DoctorFilterForm(forms.Form):
    specialization = forms.ModelChoiceField(queryset=SpecializationCategory.objects.all(), label='Specialization', empty_label='All', required=False)