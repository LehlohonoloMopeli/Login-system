
def validate_password_match(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False
    