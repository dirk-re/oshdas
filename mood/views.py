from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import MoodEntryForm
from .models import MoodAnswer, MoodRecord


class MoodEntryView(LoginRequiredMixin, FormView):
    form_class = MoodEntryForm
    template_name = "mood/form.html"
    success_url = "/mood/"

    def form_valid(self, form):
        record = MoodRecord.objects.create(user=self.request.user)
        for question, field_name in form.question_fields:
            MoodAnswer.objects.create(
                record=record,
                question=question,
                value=form.cleaned_data[field_name],
            )
        messages.success(self.request, "Gemütszustand wurde gespeichert.")
        return redirect(self.success_url)
