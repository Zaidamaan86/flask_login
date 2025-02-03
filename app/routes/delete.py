from flask import Blueprint, request, url_for, redirect, flash
from app.models import User  # Import the User model
from app import db  # Import the database instance

delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/login/delete', methods=['POST'])
def delete():
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('Account deleted successfully.')
        return redirect(url_for('landing.landing'))
    else:
        flash('Account not found.')
        return redirect(url_for('login.login'))
