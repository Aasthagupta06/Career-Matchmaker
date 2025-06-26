from django.db import models
from django.contrib.auth.models import User
import datetime; datetime.datetime.now()

# Create your models here.
class CareerSurvey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.TextField()
    skills = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Survey"
    
class Career(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    related_interests = models.TextField(help_text="Comma-separated interests")
    required_skills = models.TextField(help_text="Comma-separated skills")

    def __str__(self):
        return self.name     
