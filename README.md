# access-control
Designing and Implementing a User Authentication and Access Control Prototype

## Installing the Application
Download and unzip the '.zip' folder.
Navigate to the application directory.
```console
cd access-control
```

## Dependencies
Requires python=3.8.5 

## Running the Application

### Execute the main app:
```console
python3 -m app
```

### Execute the test suite:
```console
python3 -m  unittest -b -v
```

## File Structure
```
access-control
|   .gitignore
|   LICENSE
|   README.md
|
+---app
|       accesscontrol.py
|       enrolment.py
|       login.py
|       pwdfile.py
|       __init__.py
|       __main__.py
|
+---etc
|       blocklist.txt
|       passwd.txt
|
\---tests
        test_accesscontrol.py
        test_enrolment.py
        test_login.py
        test_pwdfile.py
        __init__.py
        __main__.py
```

## File description
* `accesscontrol.py` : Implementation of the access control mechanism
* `pwdfile.py` : Implementation of the hash function and the password file
* `enrolment.py` : Implementation of the enrolment mechanism and the proactive password checker
* `login.py` : Implementation the password verification mechanism and enforcement of the access control mechanism