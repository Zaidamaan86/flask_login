class Config:
    
    # Database URI for PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mypassword@localhost:5433/logindb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy warnings
    SECRET_KEY = 'supersecretkey'  # For Flask session security
