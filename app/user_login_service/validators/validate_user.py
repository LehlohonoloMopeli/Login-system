
def validate_email_existance(query):
    return query is not None
    
def validate_password(query, password):
    return query.password == password
    