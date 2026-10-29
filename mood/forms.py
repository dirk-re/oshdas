from django import forms

from .models import MOOD_CHOICES, MoodQuestion


class MoodEntryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question_fields = []
        for question in (
            MoodQuestion.objects.filter(is_active=True).order_by("order", "id")
        ):
            field_name = f"question_{question.pk}"
            self.fields[field_name] = forms.ChoiceField(
                label=question.text,
                choices=MOOD_CHOICES,
                widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
            )
            self.question_fields.append((question, field_name))
