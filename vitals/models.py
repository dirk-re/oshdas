from django.conf import settings
from django.db import models


class VitalMeasurement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Benutzer",
    )
    measured_at = models.DateTimeField("Zeitstempel", auto_now_add=True)
    systolic = models.PositiveSmallIntegerField("Systolisch (mmHg)")
    diastolic = models.PositiveSmallIntegerField("Diastolisch (mmHg)")
    pulse = models.PositiveSmallIntegerField("Puls (Schläge/Min.)")
    body_temperature = models.DecimalField(
        "Körpertemperatur (°C)", max_digits=4, decimal_places=1
    )

    class Meta:
        ordering = ["-measured_at"]

    def __str__(self):
        return f"{self.user.username} – {self.measured_at:%Y-%m-%d %H:%M}"
