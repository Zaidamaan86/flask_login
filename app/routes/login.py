from flask import Blueprint, render_template, request, url_for


login_bp = Blueprint('login', __name__)


@login_bp.route('/login')
def login():
    return "login"
