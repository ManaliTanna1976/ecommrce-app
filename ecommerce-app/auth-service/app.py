from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/auth_db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')
