from flask import Flask

app = Flask(__name__)


from app.routes.landing_page import landing_bp
# Import routes after initializing the app
from app.routes.signup import signup_bp

from app.routes.login import login_bp

from app.routes.delete import delete_bp

# Register blueprints
app.register_blueprint(login_bp)
app.register_blueprint(landing_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(signup_bp)


