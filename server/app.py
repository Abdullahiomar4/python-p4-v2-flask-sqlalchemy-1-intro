# server/app.py

from flask import Flask
from flask_migrate import Migrate
from models import db

# Create a Flask application
app = Flask(__name__)

# Configure database URI (SQLite in instance folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize SQLAlchemy with app
db.init_app(app)

# Optional: simple route to test server
@app.route('/')
def home():
    return "Flask-SQLAlchemy app is running!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
