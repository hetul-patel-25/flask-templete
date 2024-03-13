from flask import request,Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from app.models.user_model import Users
from app.extensions import sql_db
import uuid

def register_user():
    current_user=None
    data=request.form
    user_name=data.get('username')
    password=data.get('password')
    admin=data.get('admin')

    if request.method=="POST":
        data=request.form
        if admin=="true":
            admin=True
        else:
            admin=False
        user=Users(name=user_name,password=generate_password_hash(password),public_id=str(uuid.uuid4()),admin=admin)
        sql_db.session.add(user)
        sql_db.session.commit()
        return redirect(url_for('auth.signup'))
    return render_template('auth_template/register.html',current_user=current_user)
