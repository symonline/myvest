from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apvest_admin:Symbolo2@@localhost/apvest_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    # Create tables
    db.create_all()

    # Run in debug mode
    # Go!
    app.run(debug=True)






