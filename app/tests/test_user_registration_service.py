from . import client

def test_user_registration_service_pass():
    response = client.post(
        "/register_user",
        json = {
            "full_names": "Sandile",
            "surname": "Khendle",
            "email": "skhendle@gmail.com",
            "password": "string",
            "confirm_password": "string"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "passed",
        "message": "You have successfully registered!"
    }
    
    
def test_user_registration_service_fail_1():
    """
        Description: Repeating email that alraedy exists in the database
    """
    
    response = client.post(
        "/register_user",
        json = {
            "full_names": "Lehlohonolo",
            "surname": "Mopeli",
            "email": "hloni@gmail.com",
            "password": "string",
            "confirm_password": "string"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "failed",
        "message": "User already exists!"
    }
    
    
def test_user_registration_service_fail_2():
    """
        Description: Using different passwords
    """
    
    response = client.post(
        "/register_user",
        json = {
            "full_names": "Lehlohonolo",
            "surname": "Mopeli",
            "email": "mopeli@gmail.com",
            "password": "string",
            "confirm_password": "integer"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "failed",
        "message": "Passwords do not match!"
    }
    
    
def test_user_registration_service_fail_3():
    """
        Description: Using an invalid email address without "@"
    """
    
    response = client.post(
        "/register_user",
        json = {
            "full_names": "Lehlohonolo",
            "surname": "Mopeli",
            "email": "mopeligmail.com",
            "password": "string",
            "confirm_password": "string"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "failed",
        "message": "Invalid email address!"
    }
    
    
def test_user_registration_service_fail_4():
    """
        Description: Ommit the confirm password field
    """
    
    response = client.post(
        "/register_user",
        json = {
            "full_names": "Lehlohonolo",
            "surname": "Mopeli",
            "email": "mopeligmail.com",
            "password": "string"
        }
    )
    
    assert response.status_code == 422
    