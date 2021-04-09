
def validate_email_existance(query):
    if query == None:
        return False
    else:
        return True
    
def validate_password(query, password):
    if query.password == password:
        return True
    else:
        return False
    