#! /usr/bin/python3
# -*- coding: utf-8 -*-
# app/Problem3c.py
# Part of app, a package providing enrolment mechanism and the proactive password checker.
#
# Copyright © 2023 trong0dn

import getpass
import re
from app.Problem1d import Role, capabilities
from app.Problem2c import create_record


SPECIAL_CHARACTERS = {'!', '@', '#', '$', '%', '?', '*'}
BLOCKLIST = "etc/blocklist.txt"


def enrol_user() -> None:
    """Enrolment interface of the user to the system.

    Returns:
        None
    """
    enrol = False
    while (not enrol):
        print("Finvest Holdings")
        print("Client Holdings and Information System")
        print("---------------------------------------------------")
        print(">>> ENROL <<<")
        valid_credentials = False
        while (not valid_credentials):
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            if (password_policy(username, password)):
                valid_credentials = True
                valid_gecos = False
                while (not valid_gecos):
                    gecos = input("Enter user full name: ")
                    if not (':' in gecos): # prohibit gecos containing the character delimiter
                        valid_gecos = True
                        print("FULLNAME ACCEPTED")
                    else: 
                        print("FULLNAME DENIED")
            else:
                print("Does not comply with password policy")
                
        valid_role = False
        while (not valid_role):
            print([member.name for member in Role])
            role = input("Enter role: ")
            if Role[role] in capabilities:
                valid_role = True
                print("ROLE ACCEPTED")
            else:
                print("ROLE INVALID")
        
        if (valid_credentials and valid_role):
            if (create_record(username, password, role, gecos)):
                enrol = True
                print("ENROL SUCCESS")
            else:
                print("Account already exists") 


def password_policy(username: str, password: str) -> bool:
    """Describes the proactive password policy checking.

    Args:
        username (str): The unique id of the user.
        password (str): The plaintext password of the user.

    Returns:
        bool: True if the password adheres to the policy, otherwise False. 
   """
    if (
        (isinstance(password, str) and len(password) >= 8 and len(password) <= 12) and # must be least 8-12 characters in length
        any(x.isupper() for x in password) and # include at least one upper-case letter
        any(x.islower() for x in password) and # include at least one lower-case letter
        any(x.isdigit() for x in password) and # include at least one numerical digit
        any(x in SPECIAL_CHARACTERS for x in password) and # include at least one special character
        not (password == username) and # matching the user ID must be prohibited
        not (':' in password or ':' in username) # username or password containing the character delimiter prohibited
    ):
        if (
            (not password == username) or # matching the user ID must be prohibited
            (not (':' in password or ':' in username)) or # username or password containing the character delimiter prohibited
            (not re.search("^\d{4}-\d{2}-\d{2}$", password)) or # format of calendar dates prohibited
            (not re.search("^[A-Z0-9]{7}$", password)) or  # format of license plate numbers prohibited
            (not re.search("^\d{3}-\d{4}$", password))   # format of telephone numbers prohibited
            (not re.search("^\d{5-12}$", password)) # common numbers must be prohibited
        ):
            with open(BLOCKLIST, 'r') as file:
                blocklist = file.read()
                file.close()
                if password in blocklist: # common weak passwords must be prohibited
                    return False
                else:
                    return True
    return False


def add_disallowed_password(password: str) -> bool:
    """Add a disallowed password to the blocklist of paswords.

    Args:
        password (str): The plaintext of the disallowed password.

    Returns:
        bool: True if the password was added to the blocklist, otherwise False. 
   """
    with open(BLOCKLIST, 'r+') as file:
        blocklist = file.read()
        if password in blocklist:
            file.close()
            return False
        else:
            file.write(str(password) +'\n')
            file.close()
            return True      


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :