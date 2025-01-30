from flask import Blueprint, render_template, request, url_for


signup_bp = Blueprint('signup', __name__)


@signup_bp.route('/signup')
def landing():
    return "Signup User"
    