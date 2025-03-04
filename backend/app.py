import os
from flask_migrate import Migrate
from flask import Flask
from dotenv import load_dotenv
from database.db import db
from services.startups.startup_routes import startup_bp
from services.technologies.technology_routes import technology_bp
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(startup_bp)
app.register_blueprint(technology_bp)

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG", "False") == "True")
