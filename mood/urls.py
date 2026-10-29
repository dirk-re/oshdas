from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoodEntryView.as_view(), name="create"),
]
app_name = "mood"
