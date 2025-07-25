# 🏫 Django ERP Demo

A basic ERP (Enterprise Resource Planning) system built using Django.  
This project demonstrates simple user authentication and CRUD (Create, Read, Update, Delete) operations for managing students and faculty.

---

## 📋 Features

-  User Signup, Login, Logout (Django Auth System)
-  Student Management (Add/Delete)
-  Faculty Management (Add/Delete)
-  Authentication-protected dashboard views
-  Data storage using Django ORM and SQLite3
-  Admin Panel enabled for superusers

---

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite3
- **Frontend**: HTML, CSS (Basic templates)
- **Auth**: Django's built-in authentication system

---

## Installation

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/being-souL1230/django_erp_demo.git
cd django_erp_demo
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Environment
Windows:
```bash
venv\Scripts\activate
```
Linux:
```bash
source venv/bin/activate
```

### 4. Install Requirements
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

Now visit:
http://127.0.0.1:8000/

### Project Structure

django_erp_demo/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── db.sqlite3
├── venv/ (ignored)
│
├── my_first_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── myapp/
    ├── migrations/
    ├── templates/
    ├── static/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── forms.py

 ###Future Features (Planned)
 
- Assignment Upload/Track

- Attendance System

- Marks & Report Cards

- Notifications

### License
This project is for educational/demo purposes.
Feel free to fork and extend as needed.

### Author
Rishab aka being-souL1230
