from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import inspect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app.models import User
        db.create_all()
        print("Database initialized.")


        # Import routes after initializing the app
        from app.routes.landing_page import landing_bp
        from app.routes.signup import signup_bp
        from app.routes.login import login_bp
        from app.routes.delete import delete_bp

        # Register blueprints
        app.register_blueprint(login_bp)
        app.register_blueprint(landing_bp)
        app.register_blueprint(delete_bp)
        app.register_blueprint(signup_bp)

    return app


