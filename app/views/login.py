from flask import request,render_template,redirect,url_for,session,make_response,flash
from app.models.user_model import Users
from werkzeug.security import check_password_hash
from app import app
import jwt  
import datetime

def login_view():
    if request.method=="POST":
        try:
            data=request.form 
            user=Users.query.filter_by(name=data.get('username')).first()
            # breakpoint()
            if check_password_hash(user.password,data.get('password')):
                try:
                     access_token=jwt.encode({'public_id':user.public_id,'exp':datetime.datetime.now()+datetime.timedelta(hours=2)},app.config['SECRET_KEY'],"HS256")
                     response = make_response(redirect(url_for("home_view")))
                     response.headers["Authorization"] = access_token
                     response.set_cookie("Authorization",access_token)
                     flash('You were successfully logged in')
                     return response
                except Exception as e:
                    print("eroror==================",e)

            else:
                return redirect(url_for('auth.signup'))
        except Exception as e:
            return render_template('error/temp.html')
    
    return render_template('auth_template/login.html',current_user=None) 