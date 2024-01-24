from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from .forms import AppointmentForm


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
