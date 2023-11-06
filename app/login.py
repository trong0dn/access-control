#! /usr/bin/python3
# -*- coding: utf-8 -*-
# app/login.py
# Part of app, a package providing password verification mechanism.
#
# Copyright © 2023 trong0dn

import sys
import getpass
from datetime import datetime
from app.accesscontrol import Role
from app.pwdfile import verify_credential, retrieve_record
from app.enrolment import enrol_user


def login_user() -> None:
    """Login user to the system.

    Returns:
        None
    """
    login = False
    while (not login):
        print("Finvest Holdings")
        print("Client Holdings and Information System")
        print("---------------------------------------------------")
        print(">>> LOGIN <<<")
        valid_credentials = False
        while (not valid_credentials):
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            if (verify_credential(username, password)):
                valid_credentials = True
                print("CREDENTIAL VERIFIED")
            else:
                print("CREDENTIAL INCORRECT")

        if (valid_credentials):
            role = Role[retrieve_record(username, password)]
            if (enforce_access_control(role)):
                login = True
                print(f'> Username: {username}')
                print(f'> Role: {role}')
                print(f'> Permissions: {role.value}')


def enforce_access_control(role: str) -> bool:
    """Enforce the access control mechanism.

    Args:
        role (Role): The role of a user has in the system.

    Returns:
        bool: True if the access control permission is granted, otherwise False. 
   """
    if (Role[role] == Role['teller'] and ((datetime.now().hour < 8) or (datetime.now().hour > 17))):
        print("Tellers can only access the system during business hours from 9:00AM to 5:00PM.")
        return False
    elif (Role[role] == Role['compliance_officer']):
        # Compliance Officers can validate modifications to investment portfolios.
        return True
    elif (Role[role] == Role['technical_support']):
        # Technical Support must request client account access to troubleshoot client's technical issues.
        return True
    else: 
        return True


def user_interface() -> None:
    """A basic user interface to prototype the system.
    
    Returns:
        None
    """
    while (True):
        print("Finvest Holdings")
        print("Client Holdings and Information System")
        print("---------------------------------------------------")
        print("[1] login")
        print("[2] enrol")
        print("[3] exit")
        command = input("Enter command #: ")
        if (command == '1' or command == 'login'):
            login_user()
        elif (command == '2' or command == 'enrol'):
            enrol_user()
        elif (command == '3' or command == 'exit'):
            sys.exit()
        else:
            print("INVALID COMMAND")


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :