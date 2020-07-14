
def validate_username(username):
    if username == "":
        return {"username_error":"Field can not be empty"}

    if len(username) <= 2 or len(username) > 20:
        return {"username_error":"Username is out of range 3-20"}

    if username.count(" ") > 0:
        return {"username_error":"Username can not have spaces"}
    
    return None


def validate_email(email):
    if len(email) > 0 and len(email) < 4:
        return  {"email_error":"email must have more than 3 characters"}

    if len(email) > 20:     
        return {"email_error":"email must be less than 20 characters"}

    if (email.count(".") == 0 or email.count("@") == 0) and len(email) > 0: 
        return  {"email_error":"email must have a valid address"}

    return None



def validate_password(password, verify_password):
    if password == "":
        return {"password_error":"Field can not be empty"}

    if len(password) < 4 or len(password) > 20:
        return {"password_error":"Password is out of range 3-20"}

    if password.count(" ") > 0:
        return {"password_error":"Password can not have spaces"}

    if password != verify_password:
        return {"password_error":"Passwords do not match", "verify_error":"Passwords do not match"}
    
    return None