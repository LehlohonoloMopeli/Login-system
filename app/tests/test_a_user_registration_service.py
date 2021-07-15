from . import client

def test_user_registration_service_pass():
    response = client.post(
        "/register_user",
        json = {
            "full_names": "Lehlohonolo",
            "surname": "Mopeli",
            "id_number": "98011253940800",
            "cell_number": "0731658597",
            "email": "hloni@gmail.com",
            "password": "12345",
            "confirm_password": "12345"
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
            "id_number": "98011253940800",
            "cell_number": "0731658597",
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
            "id_number": "98011253940800",
            "cell_number": "0731658597",
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
            "id_number": "98011253940800",
            "cell_number": "0731658597",
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
            "id_number": "98011253940800",
            "cell_number": "0731658597",
            "email": "mopeligmail.com",
            "password": "string"
        }
    )
    
    assert response.status_code == 422
    