
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, auth, db

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = auth.get_user_by_email(username)
    if user:
        phone_number = user.phone_number
        if phone_number:
            return redirect(url_for('verify', username=username))
        else:
            auth.update_user(user, {'phone_number': request.form['phone_number']})
            return redirect(url_for('verify', username=username))
    else:
        return render_template('index.html', message='Invalid credentials')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        return render_template('verify.html')
    else:
        username = request.form['username']
        code = request.form['code']
        user = auth.get_user_by_email(username)
        if user:
            credential = auth.PhoneAuthProvider.credential(user.phone_number, code)
            auth.update_current_user(credential)
            return redirect(url_for('dashboard'))
        else:
            return render_template('verify.html', message='Invalid code')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        phone_number = request.form['phone_number']
        user = auth.create_user(email=username, password=password)
        auth.update_user(user, {'phone_number': phone_number})
        return redirect(url_for('verify', username=username))

@app.route('/dashboard')
def dashboard():
    user = auth.get_current_user()
    return render_template('dashboard.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
