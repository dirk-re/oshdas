from django import forms

from .models import VitalMeasurement


class VitalMeasurementForm(forms.ModelForm):
    class Meta:
        model = VitalMeasurement
        fields = ["systolic", "diastolic", "pulse", "body_temperature"]
        widgets = {
            "systolic": forms.NumberInput(attrs={"class": "form-control", "min": 50, "max": 300}),
            "diastolic": forms.NumberInput(attrs={"class": "form-control", "min": 30, "max": 200}),
            "pulse": forms.NumberInput(attrs={"class": "form-control", "min": 20, "max": 250}),
            "body_temperature": forms.NumberInput(
                attrs={"class": "form-control", "min": 30, "max": 45, "step": 0.1}
            ),
        }
