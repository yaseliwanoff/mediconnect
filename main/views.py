from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import *
from .forms import AppointmentForm, RegisterUserForm, AuthenticationForm, DoctorFilterForm, CallbackForm
from django.urls import reverse_lazy


class Main(ListView):
    template_name = 'main/main-page.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        return Doctor.objects.all()[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specializations'] = SpecializationCategory.objects.all()
        context['callback_form'] = CallbackForm()
        return context

    def post(self, request, *args, **kwargs):
        callback_form = CallbackForm(request.POST)
        if callback_form.is_valid():
            callback_form.save()  # Сохраняем данные формы, если форма валидна
            return redirect(request.path)  # Перенаправляем пользователя на ту же страницу после успешной отправки формы
        else:
            # Если форма не валидна, мы можем передать её обратно в контекст шаблона,
            # чтобы отобразить ошибки в шаблоне
            return self.get(request, *args, **kwargs)


class DoctorInfo(DetailView):
    model = Doctor
    form_class = AppointmentForm
    template_name = 'main/doc-info.html'
    context_object_name = 'doctor'
    pk_url_kwarg = 'doctor_id'
    success_url = 'DoctorList'

    def get_initial(self):
        doctor_id = self.kwargs['doctor_id']
        doctor = get_object_or_404(Doctor, id=doctor_id)
        return {'doctor': doctor, 'user': self.request.user}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppointmentForm(initial=self.get_initial())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, initial=self.get_initial())
        # Получаем объект доктора из базы данных
        doctor_id = self.kwargs['doctor_id']
        doctor = get_object_or_404(Doctor, id=doctor_id)
        # Заполняем поле доктора в форме
        form.instance.doctor = doctor
        # Заполняем поле пользователя в форме
        form.instance.user = self.request.user

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


class UserAppointmentsListView(LoginRequiredMixin, ListView):
    template_name = 'main/user-appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.filter(appointment__user=self.request.user).distinct()
        # context['filter_form'] = AppointmentDoctorFilterForm(user=self.request.user)
        return context


class DoctorListView(ListView):
    model = Doctor
    template_name = 'main/doctor-list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_filter = self.request.GET.get('specialization')
        if specialization_filter:
            queryset = queryset.filter(specialization__id=specialization_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = DoctorFilterForm(self.request.GET)
        return context


def ContactView(request):
    return render(request, 'main/contacts.html')
