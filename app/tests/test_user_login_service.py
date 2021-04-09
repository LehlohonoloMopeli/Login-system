from . import client

def test_user_login_service_pass():
    response = client.post(
        "/login",
        json = {
            "email": "hloni@gmail.com",
            "password": "string"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "user_id": 1,
        "full_names": "Lehlohonolo",
        "surname": "Mopeli",
        "email": "hloni@gmail.com"
    }
    
    
def test_user_login_service_fail_1():
    """
        Description: Using non-existant login details
    """
    response = client.post(
        "/login",
        json = {
            "email": "mopeli@gmail.com",
            "password": "integer"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "failed",
        "message": "Email or Password is incorrect!"
    }
    
    
def test_user_login_service_fail_2():
    """
        Description: Using wrong password
    """
    response = client.post(
        "/login",
        json = {
            "email": "hloni@gmail.com",
            "password": "integer"
        }
    )
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "failed",
        "message": "Email or Password is incorrect!"
    }
    
    
def test_user_login_service_fail_3():
    """
        Description: Submit email pnly
    """
    response = client.post(
        "/login",
        json = {
            "email": "hloni@gmail.com"
        }
    )
    
    assert response.status_code == 422