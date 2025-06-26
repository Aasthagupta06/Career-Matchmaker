from django.contrib import admin
from .models import CareerSurvey

# Register your models here.
from django.contrib import admin
from .models import CareerSurvey, Career

@admin.register(CareerSurvey)
class CareerSurveyAdmin(admin.ModelAdmin):
    list_display = ('user', 'interests', 'skills', 'submitted_at')
    search_fields = ('user__username', 'interests', 'skills')
    list_filter = ('submitted_at',)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'related_interests', 'required_skills')
    search_fields = ('name', 'related_interests', 'required_skills')