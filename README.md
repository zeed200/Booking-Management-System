# 🏡 Apartment & Chalet Booking System

A web-based booking system for apartments and chalets, built with Django.  
It allows customers to browse available units, select service packages, make bookings, and access them via QR codes.  
Admins can manage bookings, customer accounts, reports, and financial operations.

---

## 🚀 Features

- 🏠 Browse and book apartments or chalets
- 📦 Choose between different service packages per chalet
- 👤 Customer account creation and profile management
- 🧾 View and manage invoices and booking history
- 📊 Generate reports for bookings and revenue
- 🔐 Admin dashboard for managing units, users, and reservations
- 📲 Access booking details via QR code
- ⚡ Real-time interactions using AJAX

---

## 🛠 Tech Stack

- **Backend**: Django, Django Admin
- **Database**: SQLite 
- **Frontend**: HTML, Bootstrap, JavaScript, AJAX
- **Other**: qrcode (Python library)

---

## ⚙️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/zeed200/Booking-Management-System.git
cd Booking-Management-System
```
### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```   
### 6. Run the Development Server
```bash
python manage.py runserver
```
### 7. Access the Application
   
- Frontend: http://127.0.0.1:8000
- Admin Panel: http://127.0.0.1:8000/admin 
