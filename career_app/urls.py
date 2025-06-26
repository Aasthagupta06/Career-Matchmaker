from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('survey/', views.survey_view, name='survey'),
    path('recommendations/', views.recommendation_view, name='recommendations'),
    path('retake-survey/', views.retake_survey_view, name='retake_survey'),
    path('get-started/', views.get_started, name='get_started'),  # New URL for Get Started page

]

