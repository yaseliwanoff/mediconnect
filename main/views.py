from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import *
from .forms import AppointmentForm, RegisterUserForm, AuthenticationForm
from django.urls import reverse_lazy


class DoctorList(ListView):
    model = Doctor
    template_name = 'main/main-page.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        return Doctor.objects.all()


class DoctorInfo(DetailView):
    model = Doctor
    form_class = AppointmentForm
    template_name = 'main/doc-info.html'
    context_object_name = 'doctor'
    pk_url_kwarg = 'doctor_id'
    success_url = 'DoctorList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor_id = self.kwargs['doctor_id']
        doctor = get_object_or_404(Doctor, id=doctor_id)
        patient = None
        context['form'] = AppointmentForm(initial={'doctor': doctor, 'patient': patient})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)


class RegisterFormView(CreateView):
    form_class = RegisterUserForm
    model = User
    success_url = reverse_lazy('Login')
    template_name = 'main/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        return super().form_valid(form)


def my_logout_view(request):
    logout(request)
    return redirect('Home')
