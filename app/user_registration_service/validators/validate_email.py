
def validate_email_existance(query):
    if query == None:
        return True
    else:
        return False
    
def validate_email_format(email):
    emailAsList = []
    for i in email:
        emailAsList.append(i)
    
    if "@" in emailAsList:
        return True
    else:
        return False
    