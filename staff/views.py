from django.views.generic import ListView
from main.models import Appointment
from django.db.models import Sum



class Main(ListView):
    template_name = 'staff/main_page.html'
    context_object_name = 'appointment'
    paginate_by = 10

    def get_queryset(self):
        return Appointment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Вычисляем общее количество записей
        total_appointments = Appointment.objects.count()
        # Вычисляем сумму цен всех записей
        total_price_all = Appointment.objects.aggregate(total_price=Sum('doctor__visit_price'))['total_price']
        # Передаем значения в контекст шаблона
        context['total_appointments'] = total_appointments
        context['total_price_all'] = total_price_all or 0  # Если нет записей, установите значение по умолчанию как 0
        return context
