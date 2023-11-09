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
|       Problem1d.py
|       Problem2c.py
|       Problem3c.py
|       Problem4c.py
|       __init__.py
|       __main__.py
|
+---etc
|       blocklist.txt
|       passwd.txt
|
\---tests
        test_Problem1e.py
        test_Problem2d.py
        test_Problem3c.py
        test_Problem4c.py
        __init__.py
        __main__.py
```

## File description
* `Problem1d.py` : Implementation of the access control mechanism
* `Problem2c.py` : Implementation of the hash function and the password file
* `Problem3c.py` : Implementation of the enrolment mechanism and the proactive password checker
* `Problem4c.py` : Implementation the password verification mechanism and enforcement of the access control mechanism