from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import VitalMeasurementForm
from .models import VitalMeasurement


class VitalMeasurementCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = VitalMeasurement
    form_class = VitalMeasurementForm
    template_name = "vitals/form.html"
    success_url = reverse_lazy("vitals:create")
    success_message = "Werte wurden gespeichert."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
