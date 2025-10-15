# 🏥 Hospital Appointment Management System

# Project Description

This is a web-based Hospital Appointment Management System built using Django. The system allows patients to register, log in, and schedule appointments with doctors. Doctors can manage their own appointments, while the admin oversees the entire system.

The system is designed to simplify appointment booking, reduce administrative workload, and provide an organized view of upcoming appointments. Future improvements include email notifications and doctor-specific dashboards.

# Getting Started

●To explore the Hospital Appointment App:

# ERD
● ![ERD](static/images/ERD.png)

# Installation & Setup

 ● Clone the Repository

   git clone https://github.com/Tamara-dw/Capstone-Project.git
   cd Capstone-Project


  ●Create & Activate Virtual Environment

   python -m venv venv
   #Windows:
   venv\Scripts\activate
   #Mac/Linux:
   source venv/bin/activate


 ● Install Dependencies

   pip install -r requirements.txt


  ●Setup PostgreSQL Database

   CREATE DATABASE hospital_db;
   CREATE USER hospital_user WITH PASSWORD 'yourpassword';
   GRANT ALL PRIVILEGES ON DATABASE hospital_db TO hospital_user;


  ●Update settings.py

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hospital_db',
        'USER': 'hospital_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
       }
   }


 ● Apply Migrations

   python manage.py makemigrations
   python manage.py migrate


 ● Create Superuser

   python manage.py createsuperuser


  ●Run the Server

   python manage.py runserver


  ●Visit:

  Main site: http://127.0.0.1:8000/

  Admin panel: http://127.0.0.1:8000/admin/


# User Stories
● Patient

● Can register and log in to the system.

● Can view available doctors and schedule appointments.

● Can view, edit, or cancel their own appointments.


● Admin

● Can manage doctors, patients, and appointments.

● Can view all system data via the Django Admin Panel.

● Has full CRUD control over all entities.

# Key Features

✅ Patient registration and login

✅ Appointment creation, editing, and deletion

✅ Dashboard to view upcoming appointments (sorted by date)



# Challenges & Solutions

● Displaying appointments in chronological order	Used order_by('appointment_datetime') in DashboardView

● Keeping user-specific appointments only	Filtered appointments by patient=self.request.user in the views

# Future Improvements

● Allow doctors to have their own login and manage their schedules.

● Add email notifications for upcoming appointments.

● Enhance dashboard UX with interactive calendar view.