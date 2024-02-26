from django import forms
from .models import SpecializationCategory

from django import forms
from .models import Appointment, User, SpecializationCategory, Callback, Doctor, AppointmentTime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import DateInput


# class RegisterUserForm(UserCreationForm):
#     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
#     first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'reg-user'}))
#     last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'reg-user'}))
#     date_of_birth = forms.DateField(label='Date of birth', widget=DateInput(
#         attrs={'class': 'reg-user', 'type': 'date'}))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'reg-user'}))
#     phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'reg-user'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))
#     password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))

#     class Meta:
#         model = User
#         fields = (
#         'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'username', 'password1', 'password2')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    date_of_birth = forms.DateField(label='Date of birth', widget=DateInput(
                                                                            attrs={'class': 'reg-user', 'type': 'date', 'placeholder': ''}), initial=None, required=False)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'reg-user', 'placeholder': ''}))

    class Meta:
        model = User
        fields = (
        'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user', 'placeholder': ''}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user', 'placeholder': ''}))


class AppointmentForm(forms.ModelForm):
    day = forms.DateField(label='Appointment day', widget=forms.TextInput(attrs={'type': 'date'}))
    time = forms.ModelChoiceField(queryset=AppointmentTime.objects.all(), label='Appointment time', required=False)

    class Meta:
        model = Appointment
        fields = ['day', 'time']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Извлекаем пользователя из kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Присваиваем пользователя экземпляру Appointment
        if commit:
            instance.save()
        return instance


class DoctorFilterForm(forms.Form):
    specialization = forms.ModelChoiceField(queryset=SpecializationCategory.objects.all(), label='Specialization',
                                            empty_label='All', required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #.
        self.fields['specialization'].attrs = {'class': 'filter'}


class AppointmentDoctorFilterForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), label='Select Doctor')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['doctor'].queryset = Doctor.objects.filter(appointment__user=user).distinct()


class CallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ('name', 'email', 'phone', 'date')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Используем HTML элемент input типа date
        }
