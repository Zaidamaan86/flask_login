from flask import Blueprint, render_template, request, url_for


delete_bp = Blueprint('delete', __name__)


@delete_bp.route('/login/delete')
def delete():
    return "Delete User"
    