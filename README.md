🏥 Hospital Appointment Management System
📘 Project Overview

This project is a web-based Hospital Appointment Management System built using Django.
It allows patients to register, log in, and schedule appointments with doctors.
Doctors can manage their appointments, while the admin oversees the entire system.

The system is designed to simplify the appointment booking process and reduce administrative workload for healthcare providers.

🧠 Tech Stack

Python (Backend logic)

Django (Web framework)

PostgreSQL (Database)

HTML5 (Structure)

CSS3 (Styling)

🗂️ Data Model (ERD Overview)

![ERD Diagram](static/images/ERD.png)


⚙️ Installation & Setup Guide (with PostgreSQL)
1️⃣ Clone the Repository
git clone https://github.com/Tamara-dw/Capstone-Project.git
cd Capstone-Project

2️⃣ Create & Activate Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup PostgreSQL Database
CREATE DATABASE hospital_db;
CREATE USER hospital_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE hospital_db TO hospital_user;

5️⃣ Update settings.py
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

6️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

7️⃣ Create Superuser
python manage.py createsuperuser

8️⃣ Run the Server
python manage.py runserver


Visit:

Main site: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

👩‍⚕️ User Stories
Patient

Can register and log in to the system.

Can view available doctors and schedule appointments.

Can view, edit, or cancel their own appointments.


Admin

Can manage doctors, patients, and appointments.

Can view all system data from the Django Admin Panel.

Has full control over CRUD operations.

💡 Key Features

✅ Patient registration and login
✅ Appointment creation, editing, and deletion
✅ Dashboard to view upcoming appointments (sorted by date)
✅ Doctor management (name, specialization, contact info)
✅ Secure authentication using Django’s built-in system
✅ PostgreSQL database integration

🧩 Challenges & Solutions

Displaying appointments in chronological order	Used order_by('appointment_datetime') in the DashboardView

Keeping user-specific appointments only	Filtered appointments by patient=self.request.user in the views

🧠 Future Improvements

Allow doctors to have their own login and manage their schedules.

Add email notifications for upcoming appointments.

Store and send messages from the “Contact Us” form.