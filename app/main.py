from fastapi import FastAPI
from app.database import Engine, base
from app.routers import Auth, bookings, classes

# Create database tables
base.metadata.create_all(bind=Engine)

app = FastAPI(
    title="Fitness studio booking API",
    description="Backend API for a fitness studio class booking",
    version="1.0.0"
)

# Include routers
app.include_router(Auth.router)
app.include_router(bookings.router)
app.include_router(classes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness Studio Booking API"}