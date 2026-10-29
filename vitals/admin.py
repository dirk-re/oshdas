from django.contrib import admin

from .models import VitalMeasurement


@admin.register(VitalMeasurement)
class VitalMeasurementAdmin(admin.ModelAdmin):
    list_display = ("user", "measured_at", "systolic", "diastolic", "pulse", "body_temperature")
    list_filter = ("user",)
