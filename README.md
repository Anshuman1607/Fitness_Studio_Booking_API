# 🏋️ Fitness Studio API

## 📖 Project Overview
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

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fitness-studio-api.git
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
