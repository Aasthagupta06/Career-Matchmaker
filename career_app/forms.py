# from django import forms
# from .models import CareerSurvey

# class CareerSurveyForm(forms.ModelForm):
#     class Meta:
#         model = CareerSurvey
#         fields = ['interests', 'skills']
#         widgets = {
#             'interests': forms.TextInput(attrs={'class': 'form-control'}),
#             'skills': forms.TextInput(attrs={'class': 'form-control'}),
#         }

from django import forms

class SkillForm(forms.Form):
    skill = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a skill'})
    )

class InterestForm(forms.Form):
    interest = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter an interest'})
    )
