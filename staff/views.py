from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from main.models import Appointment, Room
from django.db.models import Sum
from .forms import DateSelectForm
from datetime import datetime
from django.urls import reverse
from main.models import Doctor


class MainPageView(ListView):
    template_name = 'staff/main-staff.html'
    context_object_name = 'appointment'
    paginate_by = 3
    form_class = DateSelectForm

    def get_queryset(self):
        queryset = Appointment.objects.all()
        selected_date = self.request.GET.get('selected_date')
        if selected_date:
            queryset = queryset.filter(appointment_day=selected_date)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_date = self.request.GET.get('selected_date')
        context['filter_form'] = self.get_form()
        context['total_appointments'] = Appointment.objects.filter(appointment_day=selected_date).count()
        context['total_price_all'] = Appointment.objects.filter(appointment_day=selected_date).aggregate(
            total_price=Sum('doctor__visit_price'))['total_price'] or 0
        context['doctors'] = Doctor.objects.all()
        return context

    def get_form(self):
        return self.form_class(self.request.GET)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            if selected_date:
                return HttpResponseRedirect(reverse('AdminMain') + f'?selected_date={selected_date}')
        return self.get(request, *args, **kwargs)


class AppointmentHistoryView(ListView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'staff/appointment-history.html'
    paginate_by = 10
    form_class = DateSelectForm

    def get_queryset(self):
        queryset = Appointment.objects.all()
        selected_date = self.request.GET.get('selected_date')
        if selected_date:
            queryset = queryset.filter(appointment_day=selected_date)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_date = self.request.GET.get('selected_date')
        context['filter_form'] = self.get_form()
        context['total_appointments'] = Appointment.objects.count()
        context['total_price_all'] = Appointment.objects.aggregate(total_price=Sum('doctor__visit_price'))['total_price'] or 0
        context['doctors'] = Doctor.objects.all()
        return context

    def get_form(self):
        return self.form_class(self.request.GET)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            if selected_date:
                return HttpResponseRedirect(reverse('AdminMain') + f'?selected_date={selected_date}')
        return self.get(request, *args, **kwargs)

class ChatView(ListView):
    template_name = 'staff/chat.html'
    context_object_name = 'rooms'
    paginate_by = 5

    def get_queryset(self):
        return Room.objects.all()


class RoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, 'staff/room.html', {'room': room})


def analytics(request):
    return render(request, 'staff/analytics.html')


def callback(request):
    return render(request, 'staff/callback.html')


class DoctorAppointmentView(ListView):
    model = Appointment
    template_name = 'staff/doctor-appointment.html'
    context_object_name = 'doctor_appointments'  # Обновленное имя контекста

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        selected_date = self.request.GET.get('selected_date')

        queryset = Appointment.objects.filter(doctor_id=doctor_id)  # Фильтрация по id доктора

        if selected_date:
            queryset = queryset.filter(appointment_day=selected_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.get_form()
        context['total_appointments'] = context['doctor_appointments'].count()
        context['total_price_all'] = context['doctor_appointments'].aggregate(
            total_price=Sum('doctor__visit_price'))['total_price'] or 0
        context['doctors'] = Doctor.objects.all()
        return context

    def get_form(self):
        return DateSelectForm(self.request.GET)



