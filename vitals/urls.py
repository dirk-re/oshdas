from django.urls import path

from . import views

urlpatterns = [
    path("", views.VitalMeasurementCreateView.as_view(), name="create"),
]
app_name = "vitals"
