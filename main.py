from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', username_error="", password_error="",
    verify_error="", email_error="")

@app.route("/", methods=['POST'])
def validate_form():
    form = render_template('index.html', username_error="", password_error="",
    verify_error="", email_error="")
    username = request.form['user-name']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    if username == "":
        return render_template('index.html', username_error="Field can not be empty")
    if password == "":
        return render_template('index.html', password_error="Fields can not be empty")
    if len(password) <= 2 or len(password) > 20:
        return render_template('index.html', password_error="Password is out of range 3-20")
    if len(username) <= 2 or len(username) > 20:
        return render_template('index.html', username_error="Username is out of range 3-20")
    if password.count(" ") > 0:
        return render_template('index.html', password_error="Password can not have spaces")
    if username.count(" ") > 0:
        return render_template('index.html', username_error="Username can not have spaces")
    if password != verify_password:
        return render_template('index.html', password_error="Passwords do not match",
        verify_error="Passwords do not match")
    if len(email) > 0 and len(email) > 20:     
        return render_template('index.html', email_error="email must be less than 20 characters")
    if len(email) > 0 and len(email) <= 3:
        return render_template("index.html", email_error="email must have more than 3 characters")

    if email.count(".") or email.count("@") == 0 and len(email) > 0: 
        return render_template('index.html', email_error="email must have a valid address")
    
    else:
        return render_template('welcome.html', user=username)

app.run()

