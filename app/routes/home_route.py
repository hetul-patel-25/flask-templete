from flask import Blueprint
from app import app
from app.views import home
home_bp=Blueprint('home',__name__)

from flask import render_template,redirect,url_for
@app.route("/",methods=['GET','POST'])
def home_view():
    return home.home()