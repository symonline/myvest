from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from project.user.forms import LoginForm

from flask_bootstrap import Bootstrap

# from app import db

app = Flask(__name__)
Bootstrap(app)

@app.route('/<password>')
def index(password):
    form = LoginForm()
    hashed_value = generate_password_hash(password, method='sha256')
    return render_template('login.html', form=form)  # f'{hashed_value}'

'''
@app.route('/<password>')
def valid(password):
    index(password)
    val = check_password_hash(index,password)
    return val
'''

if __name__ == '__main__':
    app.run(debug=True)
