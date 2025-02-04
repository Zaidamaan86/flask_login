from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import User
from app import db

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        dob = request.form['dob']
        gender = request.form['gender']
        mobile_number = request.form['mobile_number']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)  # Hash the password before storing

        new_user = User(
            full_name=full_name,
            dob=dob,
            gender=gender,
            mobile_number=mobile_number,
            username=username,
            email=email,
            password=hashed_password  # Store hashed password
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login.login'))

    return render_template('signup.html')
