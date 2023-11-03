#! /usr/bin/python3
# -*- coding: utf-8 -*-
# app/pwdfile.py
# Part of app, a package providing password file mechanism.
#
# Copyright © 2023 trong0dn

import hashlib 
import uuid
from app.accesscontrol import Role


DATABASE = "etc/passwd.txt"


def create_record(username: str, password: str, role: Role) -> bool:
    """Create a new record in the database when enrolling new users.

    Args:
        username (str): The unique id of the user.
        password (str): The plaintext password of the user.
        role (Role): The role of a user has in the system.

    Returns:
        bool: True if the record has been created, otherwise False. 
   """
    with open(DATABASE, 'r') as file:
        for line in file.readlines():
            record = line.split(':')
            # Username must be unique in the existing record
            if (record[0] == username):
                return False
    file.close()
    salt = uuid.uuid4().hex
    salted_hash = hash_function(password, salt)
    add_record(username, salt, salted_hash, role)
    return True


def add_record(username: str, salt: str, salted_hash: str, role: Role) -> None:
    """Add a new record to the database.

    Args:
        username (str): The unique id of the user.
        salt (str): The universally unique identifier as hexidecimal.
        salted_hash (str): The hash of the password and the salt together.
        role (Role): The role of a user has in the system.

    Returns:
        None
   """
    with open(DATABASE, 'a') as file:
        record = f"{username}:{salt}:{salted_hash}:{role.name}\n"
        file.write(record)
        file.close()


def retrieve_record(username: str, password: str) -> str:
    """Retrieve a record from the database.

    Args:
        username (str): The unique id of the user.
        password (str): The plaintext password of the user.

    Returns:
        str: The user record role information stored within the database.
   """
    with open(DATABASE, 'r') as file:
        for line in file.readlines():
            record = line.strip('\n').split(':')
            if (record[0] == username):
                # Compute new hash of the input password against known salted hash within the record
                if (hash_function(password, record[1]) == record[2]):
                    return record[3]
    file.close()


def verify_credential(username: str, password: str) -> bool:
    """Verify username and password pair credentials exists within the database.

    Args:
        username (str): The unique id of the user.
        password (str): The plaintext password of the user.

    Returns:
        bool: True, if the username-password credential have a corresponding user record within the database, otherwise False.
   """
    with open(DATABASE, 'r') as file:
        for line in file.readlines():
            record = line.strip('\n').split(':')
            if (record[0] == username):
                # Compute new hash of the input password against known salted hash within the record
                if (hash_function(password, record[1]) == record[2]):
                    return True
    file.close()
    return False


def hash_function(password: str, salt: str) -> str:
    """Hash function using SHA-256.

    Args:
        password (str): The plaintext password of the user.
        salt (str): The universally unique identifier as hexidecimal.

    Returns:
        str: The salted hash value of the password and salt together.
   """
    return hashlib.sha256(password.encode() + salt.encode()).hexdigest()


if __name__ == '__main__':
    print(len(uuid.uuid4().hex))
    create_record("jsmith", "pwd", Role.teller)


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :