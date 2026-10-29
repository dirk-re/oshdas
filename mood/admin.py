from django.contrib import admin

from .models import MoodAnswer, MoodQuestion, MoodRecord


class MoodAnswerInline(admin.TabularInline):
    model = MoodAnswer
    extra = 0


@admin.register(MoodQuestion)
class MoodQuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(MoodRecord)
class MoodRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "recorded_at")
    inlines = [MoodAnswerInline]
