from flask import Flask, request, redirect, render_template

from scripts.validate import validate_username, validate_password, validate_email

app = Flask(__name__)
app.config['DEBUG'] = False


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html'
                            , username_error=""
                            , password_error=""
                            , verify_error=""
                            , email_error="")


@app.route("/", methods=['POST'])
def validate_form():

    username = request.form['user-name']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    # Walrus operator is only compatible with Python 3.8 and above.
    error = {} if (message := validate_username(username)) == None else message
    error = error if (message := validate_password(password, verify_password)) == None else {**error,**message}
    error = error if (message := validate_email(email)) == None else {**error,**message}

    if len(error) > 0:
        return render_template('index.html', **error)
    else:
        return render_template('welcome.html', user=username)


if __name__ == "__main__":
    app.run()

