from flask import render_template
from . import user

@user.route('/login')
def login():
    return render_template('user/login.html')