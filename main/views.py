from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import *
from .forms import AppointmentForm, RegisterUserForm, AuthenticationForm, DoctorFilterForm, CallbackForm, \
    AppointmentDoctorFilterForm
from django.urls import reverse_lazy
from django.contrib import messages


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
        return {'doctor': doctor}  # Удалите 'user' из initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppointmentForm(initial=self.get_initial(),
                                          user=self.request.user)  # Передаем пользователя в форму
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, user=request.user)  # Передаем пользователя в форму
        doctor_id = self.kwargs['doctor_id']
        doctor = get_object_or_404(Doctor, id=doctor_id)
        form.instance.doctor = doctor
        # Передайте значение времени записи в форму
        form.instance.appointment_time = get_object_or_404(AppointmentTime, id=request.POST.get('time'))

        if form.is_valid():
            appointment_day = form.cleaned_data['day']
            appointment_time = form.cleaned_data['time']
            # Проверяем, есть ли уже запись на выбранное время у данного доктора
            existing_appointments = Appointment.objects.filter(
                doctor=doctor,
                appointment_day=appointment_day,
                appointment_time=appointment_time
            )
            if existing_appointments.exists():
                # Если запись уже существует, выводим сообщение об ошибке
                messages.error(request, 'Appointment for this date and time already exists.')
                return self.get(request, *args, **kwargs)
            else:
                form.save()
                return redirect('UserPage')

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


class UserPageView(LoginRequiredMixin, ListView):
    template_name = 'main/user-appointments.html'
    context_object_name = 'appointments'
    paginate_by = 5

    def get_queryset(self):
        queryset = Appointment.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.filter(appointments__user=self.request.user).distinct()
        context['filter_form'] = AppointmentDoctorFilterForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        filter_form = AppointmentDoctorFilterForm(request.POST, user=request.user)
        if filter_form.is_valid():
            selected_doctor = filter_form.cleaned_data['doctor']
            queryset = Appointment.objects.filter(user=self.request.user, doctor=selected_doctor)
            self.object_list = queryset  # Обновляем атрибут object_list
            context = self.get_context_data(appointments=queryset, filter_form=filter_form)
            return render(request, self.template_name, context)
        else:
            return self.render_to_response(self.get_context_data())

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


@login_required
def cancel_appointment(request, appointment):
    appointment_item = get_object_or_404(Appointment, id=appointment, user=request.user)
    appointment_item.delete()
    return redirect('UserPage')


def ContactView(request):
    return render(request, 'main/contacts.html')
