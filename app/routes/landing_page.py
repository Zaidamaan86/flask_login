from flask import Blueprint, render_template, request, url_for


landing_bp = Blueprint('landing', __name__)


@landing_bp.route('/')
def landing():
    return render_template('index.html')
    