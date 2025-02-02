from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import check_password_hash
from app.models import User  # Import the User model
from app import db  # Import the database instance

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        usercheck = User.query.filter_by(username=username).first()

        if usercheck and check_password_hash(usercheck.password, password):  # Validate password
            return render_template('successfully_loggedin.html', username=usercheck.username, full_name=usercheck.full_name)
        else:
            flash('Username or Password is Wrong!')
            return redirect(url_for('login.login'))
    return render_template('login.html')  # render login.html

