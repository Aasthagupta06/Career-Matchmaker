# 🚀 Career Matchmaker

## 📝 Project Description
Career Matchmaker is a Django-based web application that helps users discover suitable career paths based on their skills and interests. Users fill out a survey, and the app uses a machine learning model to recommend careers. The platform supports user registration, login, and provides a personalized dashboard with recommendations.

## ✨ Features
- 👤 User registration and authentication
- 📝 Dynamic survey for skills and interests
- 🤖 Machine learning-powered career recommendations (SVM model with 97.78% accuracy)
- 📊 Personalized user dashboard
- 🛠️ Admin panel for user and data management
- 🗄️ PostgreSQL support for production-ready database
- 🐳 Docker support for easy deployment and development

## 🛠️ Tech Stack
- **Backend:** Django (Python) 🐍
- **Frontend:** HTML, CSS, JavaScript (Django Templates) 🎨
- **Database:** PostgreSQL 🐘 (with SQLite fallback)
- **Machine Learning:** scikit-learn, joblib, TF-IDF vectorization 🤖
- **Containerization:** Docker & Docker Compose 🐳

## 🤖 ML Model Details
- **Model Type:** Support Vector Classifier (SVM)
- **Accuracy:** 97.78% 🏆
- **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
- **Total careers classified:** 50 💼
- **Features:** Skills and interests text processing

---

## 🚀 Quick Start with Docker (Recommended)

### 🔗 Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) (usually comes with Docker Desktop)

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd career_project
```

### 2️⃣ Build and Run with Docker
```bash
# Build the Docker images
docker-compose build

# Start the application
docker-compose up
```

### 3️⃣ Access the Application
- **Main App:** [http://localhost:8000](http://localhost:8000)
- **Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)

### 4️⃣ Set Up Database (First Time Only)
```bash
# In a new terminal, run migrations
docker-compose exec web python manage.py migrate

# Create admin user (optional)
docker-compose exec web python manage.py createsuperuser
```

### 5️⃣ Stop the Application
```bash
# Stop containers
docker-compose down

# Stop and remove all data (volumes)
docker-compose down -v
```

---

## 🛠️ Traditional Setup (Without Docker)

### 🔗 Prerequisites
- Python 3.8+
- pip
- PostgreSQL (optional, SQLite works for development)

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd career_project
```

### 2️⃣ Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

#### Option A: SQLite (Default - No setup needed)
The app will work with SQLite out of the box.

#### Option B: PostgreSQL
1. Install PostgreSQL on your system
2. Create a database and user
3. Update `career_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Set Up Database
```bash
# Apply migrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure
```
career_project/
├── career_app/                 # Main Django app
│   ├── models.py              # Database models
│   ├── views.py               # Business logic and views
│   ├── urls.py                # URL routing
│   ├── templates/             # HTML templates
│   ├── ml_model/              # Machine learning models
│   │   ├── career_recommendation_model.pkl
│   │   ├── tfidf_vectorizer.pkl
│   │   ├── label_encoder.pkl
│   │   └── model_info.json
│   └── utils/                 # Utility functions
├── career_project/            # Django project settings
│   ├── settings.py           # Project configuration
│   └── urls.py               # Main URL configuration
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose setup
├── requirements.txt           # Python dependencies
└── manage.py                  # Django management script
```

---

## 🔧 Configuration

### Environment Variables (Docker)
The following environment variables are set in `docker-compose.yml`:
- `DEBUG=1` - Enable debug mode
- `DJANGO_DB_HOST=db` - Database host
- `DJANGO_DB_NAME=career_db` - Database name
- `DJANGO_DB_USER=career_user` - Database user
- `DJANGO_DB_PASSWORD=Saimandir` - Database password

### Database Configuration
- **Docker:** Uses PostgreSQL with the credentials above
- **Local:** Uses SQLite by default, or PostgreSQL if configured

---

## 🐛 Troubleshooting

### Docker Issues

#### "Port already in use" error
```bash
# Check what's using port 8000 or 5432
docker ps
# Stop conflicting containers
docker-compose down
```

#### "Module not found" errors
```bash
# Rebuild the Docker image
docker-compose build --no-cache
```

#### Database connection issues
```bash
# Check if database container is running
docker-compose ps
# View database logs
docker-compose logs db
```

### General Issues

#### Migrations not applied
```bash
# Docker
docker-compose exec web python manage.py migrate

# Local
python manage.py migrate
```

#### Static files not loading
```bash
# Docker
docker-compose exec web python manage.py collectstatic

# Local
python manage.py collectstatic
```

#### ML model not loading
- Ensure all `.pkl` files are present in `career_app/ml_model/`
- Check file permissions
- Verify the model files are not corrupted

---

## 📊 Database Management

### Access PostgreSQL (Docker)
```bash
# Connect to database shell
docker-compose exec db psql -U career_user -d career_db

# View users
SELECT username FROM auth_user;

# Exit
\q
```

### Using pgAdmin with Docker
- Host: `localhost`
- Port: `5432`
- Username: `career_user`
- Password: `Saimandir`
- Database: `career_db`

---

## 🔒 Security Notes
- Change default passwords in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Regularly update dependencies

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📝 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgments
- Django community for the excellent framework
- scikit-learn team for ML tools
- PostgreSQL community for the robust database

---

**Thank you for checking out Career Matchmaker!** 🎉

For questions or issues, please open an issue on GitHub.
