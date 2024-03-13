
import os
from flask import Flask


# def create_app():
app = Flask(__name__,
        template_folder="../templates",
        static_folder="../static",
)




SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

from app.extensions import sql_db
from app.routes.home_route import home_bp

with app.app_context():
# sql_db.drop_all()
    sql_db.create_all()

app.register_blueprint(home_bp)




