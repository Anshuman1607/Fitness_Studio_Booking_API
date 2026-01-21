#  Fitness Studio API

##  Project Overview
This project is a RESTful API built with **FastAPI (Python)** for a fictional fitness studio offering classes such as **Yoga**, **Zumba**, and **HIIT**.  

Users can:
- **Sign up** and **log in** (JWT-based authentication)
- **View all upcoming classes**
- **Create new classes** (authenticated only)
- **Book available classes** (authenticated only)
- **View their own bookings**

The API ensures:
- Secure authentication with JWT tokens
- Validation to prevent overbooking
- Clear separation of concerns (routes, models, schemas, services)

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Anshuman1607/fitness-studio-api.git
cd fitness-studio-api
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Run Locally
```bash
uvicorn app.main:app --reload
```
## API Usage

### Sign up
```bash
curl -X POST http://localhost:8000/signup \
-H "Content-Type: application/json" \
-d '{"name":"Alice","email":"alice@example.com","password":"securepass"}'
```
### Log In
```bash
curl -X POST http://localhost:8000/login \
-H "Content-Type: application/json" \
-d '{"email":"alice@example.com","password":"securepass"}'
```
### Create a Class(Authenticated)
```bash
curl -X POST http://localhost:8000/classes \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{
  "name": "Yoga Flow",
  "dateTime": "2025-06-15T10:00:00Z",
  "instructor": "John Doe",
  "availableSlots": 20
}'
```
### View All Classes
```bash
curl http://localhost:8000/classes
```
## Book a Class(Authenticated)
```bash
curl -X POST http://localhost:8000/book \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{
  "class_id": 1,
  "client_name": "Alice",
  "client_email": "alice@example.com"
}'
```
## View My Bookings(Authenticated)
```bash
curl -H "Authorization: Bearer <token>" http://localhost:8000/bookings
```
