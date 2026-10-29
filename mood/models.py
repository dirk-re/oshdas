from django.conf import settings
from django.db import models

MOOD_CHOICES = [
    (1, "sehr gut"),
    (2, "gut"),
    (3, "mittel"),
    (4, "schlecht"),
    (5, "sehr schlecht"),
]


class MoodQuestion(models.Model):
    text = models.CharField("Frage", max_length=255)
    order = models.PositiveSmallIntegerField(
        "Reihenfolge", default=0, help_text="Bestimmt die Position in der Liste."
    )
    is_active = models.BooleanField("Aktiv", default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text


class MoodRecord(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Benutzer",
    )
    recorded_at = models.DateTimeField("Zeitstempel", auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self):
        return f"{self.user.username} – {self.recorded_at:%Y-%m-%d %H:%M}"


class MoodAnswer(models.Model):
    record = models.ForeignKey(
        MoodRecord, on_delete=models.CASCADE, related_name="answers"
    )
    question = models.ForeignKey(MoodQuestion, on_delete=models.PROTECT)
    value = models.PositiveSmallIntegerField("Antwort", choices=MOOD_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["record", "question"], name="unique_answer_per_question"
            )
        ]
