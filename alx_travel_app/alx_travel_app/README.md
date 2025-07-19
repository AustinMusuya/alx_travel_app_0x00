# 🏠 Airbnb Clone Backend API

This is a Django REST Framework (DRF) based backend API for an Airbnb-style property rental platform. The system supports user registration and authentication, listing properties, making bookings, payments, and reviews.

## 🚀 Features

- JWT-based user authentication
- User registration and login
- Property listing by hosts
- Booking system for guests
- Payment tracking
- Review system for properties
- Role-based logic (Host vs Guest)

## 🛠️ Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL or SQLite (dev)
- JWT Authentication (`djangorestframework-simplejwt`)

---

## 📁 Project Structure
```bash
airbnb_clone/
├── api/
│ ├── models.py # Custom User, Property, Booking, Payment, Review
│ ├── serializers.py # DRF Serializers for all models
│ ├── views.py # API logic
│ ├── urls.py # API routes
│ ├── permissions.py # Custom permission classes
│ └── ...
├── airbnb_clone/ # Main project folder
│ └── settings.py
└── manage.py
```


## 🧑‍💻 Models

- `User`: Custom user model with `user_id` (UUID), `username`, `email`, etc.
- `Property`: Listing with name, location, price per night, etc.
- `Booking`: Date-bound reservations with status (Pending, Confirmed, Canceled)
- `Payment`: Related to bookings, records method and amount
- `Review`: Rating and comment by a guest for a property

---

## 🔐 Authentication

Authentication is handled using JWT (JSON Web Tokens). To authenticate:

1. Register via `/api/register/`
2. Login via `/api/login/`
3. Use the returned access token for authenticated endpoints.

Example Header:

```bash
Authorization: Bearer <your_access_token>
```

## 🧪 Sample API Endpoints

| Endpoint               | Method | Description                    |
|------------------------|--------|--------------------------------|
| `/api/register/`       | POST   | Register a new user            |
| `/api/login/`          | POST   | Login with email + password    |
| `/api/properties/`     | GET/POST | List or create property     |
| `/api/bookings/`       | GET/POST | List or create booking       |
| `/api/payments/`       | POST   | Make a payment                 |
| `/api/reviews/`        | POST   | Submit a property review       |

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/airbnb-clone-backend.git
cd airbnb-clone-backend

# Setup virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver