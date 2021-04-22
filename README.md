# **Login-system**


## **Programming Tools**
> Language: Python, version 3.9.0 <br> 
Framework: FastAPI<br>
Database: MySQL using SQLAlchemy models<br>
Packages used are in the requirements.txt file <br>
Actor Servers use fastApi for end points, sqlalchemy for data models and service logic, pyndatic for input and output models.
<br>

## **Coding Standards**
**Implementing and improving these standards is crucial to the development of the system. It can allow us to move to legacy mode efficiently. It's in your best interest as a contributor to follow and help improve these. Code writen by different people, will look like it was writen by a single person.**
<br>

> #### **Variables**

```python
# A variable should be descriptive enough such that, it explains its use in the context of the code. E.g:

def validate_email_format(email):
    emailAsList = []
    for i in email:
        emailAsList.append(i)
```

> #### **Functions**
```python
# Function should be named such that it describe the task it's executing. A function should execute one and only one task. E.g:
def login(self):
        
        query = self.session.query(User).filter_by(email = self.__inputs.email).first()
        
        if validate_email_existance(query) == True:
            if validate_password(query, self.__inputs.password) == True:
        
                return {
                    "user_id": query.user_id,
                    "full_names": query.full_names,
                    "surname": query.surname,
                    "email": self.__inputs.email
                }
            
            else:
                return {
                    "status": "failed",
                    "message": "Email or Password is incorrect!"
                }
        else:
            return {
                "status": "failed",
                "message": "Email or Password is incorrect!"
            }
```

> #### **Classes**
```python
# A class should be named such that it describes the object it's representing or explains the service it's implementing. 
''' 
Example of a class for creating database model can be viewed in the app/database_model/user.py file. 

Example of a class for implementing a service can be viewed in app/user_login_service/service.py  
'''

# A class must contain all the functions it needs to execute its service. 

# A class should make a call to an existing service only if the service already exists and it will need a lot of resources to execute it in the class.  
```

## **Project Structure** <br>
<ul>
    <li>app/
    <ul>
    <li>database_models/
    <ul>
        <li>__init__.py</li>
        <li>user.py</li>
    </ul>
    </li>
    <li>{system requirement description}_service/
        <ul>
            <li>validators/
            <ul>
                <li>__init__.py</li>
                <li>Python files with validators</li>
            </ul>
            </li>
            <li>__init__.py</li>
            <li>model.py    
                <blockquote>
                Contains pyndatic classes with validators, that are used as input parameters for API functions and services class.
                </blockquote>
            </li>
            <li>route.py
                <blockquote>
                Contains API router function, with its Protocol( POST, GET, DELETE or UPDATE) and calls for the service to be executed
                </blockquote>
            </li>
            <li>service.py  
                <blockquote>
                Where the logic for the system requirement is executed
                </blockquote>
            </li>
            <li>main.py     
                <blockquote>
                Allows us to run a service independently
                </blockquote>
            </li>
        </ul>
    </li>
    <li>__init__.py</li>
    <li>main.py</li>
    </ul>
    </li>
    <li>.gitignore</li>
    <li>requirements.txt</li>
    <li>README.md</li>
</ul>

## **Getting Started** <br>
```python
"""
Create a database in MySQL called "banking-app". SQLAlchemy will
    create the tables once the server runs.

"""

# Python version: 3.9.0
"MINGW64 - bash terminal"
# Run command in directory you will be working from.
$ : git clone https://github.com/LehlohonoloMopeli/banking-app.git
$ : cd banking-app

# To create virtual environment.
$ */banking-app(env): python3.9 -m venv env

# To activate virtual environment
$ */banking-app(env): source ".\env\Scripts\activate"

# To install the requirements run
$ */banking-app(env): pip  install -r requirements.txt

# To update requirements.txt after installing new package
$ */banking-app(env): pip freeze > requirements.txt

# To run the entire application use the following command
$ */banking-app(env): hypercorn app.main:app --reload

# To run a service of the application use the following command
$ */banking-app(env): hypercorn app.'service name'.main:app --reload
# E.g
$ */banking-app(env): hypercorn app.user_login_service.main:app --reload

# To deactivate virtual enviroment
$ */banking-app(env): deactivate
```