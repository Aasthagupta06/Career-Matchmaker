from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CareerSurvey, Career
from django.conf import settings
import joblib
import os
from .utils.career_info import career_descriptions
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  # optional for GET
from django.views.decorators.http import require_POST 

# ML model loading
model_path = os.path.join(settings.BASE_DIR, 'career_app', 'ml_model', 'career_recommendation_model.pkl')
vectorizer_path = os.path.join(settings.BASE_DIR, 'career_app', 'ml_model', 'tfidf_vectorizer.pkl')
encoder_path = os.path.join(settings.BASE_DIR, 'career_app', 'ml_model', 'label_encoder.pkl')
career_model = joblib.load(model_path)
tfidf_vectorizer = joblib.load(vectorizer_path)
label_encoder = joblib.load(encoder_path)

def index(request):
    return render(request, 'index.html')

def get_started(request):
    return render(request, 'get_started.html')

def login_view(request):
    print("INSIDE LOGIN VIEW", request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)

        if user is not None:
            login(request, user)
            print("Login success")
            return redirect('/dashboard/')
        else:
            print("Login failed")
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print("Registering:", username, email, password1, password2)

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1, first_name=name)
        print("User created:", user)
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('dashboard')

    return render(request, 'register.html')

  

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return redirect('dashboard')

@login_required
def dashboard(request):
    user = request.user
    try:
        survey = CareerSurvey.objects.get(user=user)
        survey_completed = bool(survey.skills and survey.interests)
        survey_progress = 100 if survey_completed else 50
        user_input = (survey.skills + ' ' + survey.interests).lower()
        user_vector = tfidf_vectorizer.transform([user_input])
        try:
            probabilities = career_model.predict_proba(user_vector)[0]
            top_indices = probabilities.argsort()[-1:][::-1]
            last_results = label_encoder.inverse_transform([top_indices[0]])[0]
        except Exception:
            last_results = None
    except CareerSurvey.DoesNotExist:
        survey = None
        survey_completed = False
        survey_progress = 0
        last_results = None
    context = {
        'survey_completed': survey_completed,
        'survey_progress': survey_progress,
        'last_results': last_results,
    }
    return render(request, 'dashboard.html', context)

@login_required
def survey_view(request):
    """
    Handles survey form with dynamic plain text fields for skills and interests.
    """
    if request.method == 'POST':
        # Get all skills and interests from the POST data (multiple fields with same name)
        skills = request.POST.getlist('skills')
        interests = request.POST.getlist('interests')
        # Remove empty strings if any
        skills = [s.strip() for s in skills if s.strip()]
        interests = [i.strip() for i in interests if i.strip()]
        
        # **Validation: At least one skill or interest required**
        if not skills and not interests:
            from django.contrib import messages
            messages.error(request, "Please add at least one skill or interest.")
            # Pass back the attempted values so user doesn't lose input
            return render(request, 'survey.html', {
                'initial_skills': [''],
                'initial_interests': [''],
            })
        
        # Save to model as comma-separated string
        survey, created = CareerSurvey.objects.get_or_create(user=request.user)
        survey.skills = ', '.join(skills)
        survey.interests = ', '.join(interests)
        survey.save()
        return redirect('recommendations')
    else:
        # Prefill if survey exists
        try:
            survey = CareerSurvey.objects.get(user=request.user)
            initial_skills = [s.strip() for s in survey.skills.split(',')] if survey.skills else ['']
            initial_interests = [i.strip() for i in survey.interests.split(',')] if survey.interests else ['']
        except CareerSurvey.DoesNotExist:
            initial_skills = ['']
            initial_interests = ['']
    return render(request, 'survey.html', {
        'initial_skills': initial_skills,
        'initial_interests': initial_interests,
    })


@login_required
def recommendation_view(request):
    try:
        survey = CareerSurvey.objects.get(user=request.user)
    except CareerSurvey.DoesNotExist:
        return render(request, 'no_survey.html')
    user_input = (survey.skills + ' ' + survey.interests).lower()
    user_vector = tfidf_vectorizer.transform([user_input])
    try:
        probabilities = career_model.predict_proba(user_vector)[0]
        top_indices = probabilities.argsort()[-3:][::-1]
        top_careers = [label_encoder.inverse_transform([i])[0] for i in top_indices]
    except Exception:
        top_careers = []
    career_info = [(career, career_descriptions.get(career, "No description available.")) for career in top_careers]
    return render(request, 'recommendation.html', {'career_info': career_info})

@login_required
def retake_survey_view(request):
    CareerSurvey.objects.filter(user=request.user).delete()
    return redirect('survey')




