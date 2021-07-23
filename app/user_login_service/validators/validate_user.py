
def validate_email_existance(query):
    return bool(query)
    
def validate_password(query, password):
    return query.password == password
    