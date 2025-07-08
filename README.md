# Career Matchmaker

## Project Description
Career Matchmaker is a Django-based web application that helps users discover suitable career paths based on their skills and interests. Users fill out a survey, and the app uses a machine learning model to recommend careers. The platform supports user registration, login, and provides a personalized dashboard with recommendations.

## Features
- User registration and authentication
- Dynamic survey for skills and interests
- Machine learning-powered career recommendations
- Personalized user dashboard
- Admin panel for user and data management
- PostgreSQL support for production-ready database

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** PostgreSQL (default: SQLite for quick start)
- **Machine Learning:** scikit-learn, joblib

## ML Model
- **Best Model:** SVM (Accuracy: 0.9937)
- **Total careers classified:** 50

## How to Run Locally

### Prerequisites
- Python 3.8+
- pip
- PostgreSQL (for production-like setup)

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd career_project(correct)
```

### 2. Set Up Virtual Environment & Install Dependencies
```sh
python -m venv venv
# Activate venv (Windows)
venv\Scripts\activate
# Activate venv (Linux/Mac)
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Database
- By default, uses SQLite. For PostgreSQL, update `career_project/settings.py` with your DB credentials.

### 4. Apply Migrations & Create Superuser
```sh
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Development Server
```sh
python manage.py runserver
```
Visit [http://localhost:8000](http://localhost:8000)

ThankYou!
