#! /usr/bin/python3
# -*- coding: utf-8 -*-
# app/Problem4c.py
# Part of app, a package providing password verification mechanism.
#
# Copyright © 2023 trong0dn

import sys
import getpass
from datetime import datetime
from app.Problem1d import Role, capabilities
from app.Problem2c import verify_credential, retrieve_record
from app.Problem3c import enrol_user


def login_user() -> None:
    """Login interface of the user to the system.

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
            gid = retrieve_record(username, password)
            role = Role(int(gid)).name
            if (enforce_access_control(role)):
                login = True
                print(f'> Username: {username}')
                print(f'> Role: {role}')
                print(f'> Permissions: {capabilities.get(Role[role])}')
            else:
                print("User does not have access")


def enforce_access_control(role: str) -> bool:
    """Enforce the access control mechanism.

    Args:
        role (str): The role of a user has in the system.

    Returns:
        bool: True if the access control permission is granted, otherwise False. 
   """
    if (Role[role] == Role['teller'] and ((datetime.now().hour < 8) or (datetime.now().hour > 17))):
        # Tellers can only access the system during business hours from 9:00AM to 5:00PM.
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