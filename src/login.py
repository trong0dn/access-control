### The password verification mechanism
import sys
import getpass
from datetime import datetime
from src.accesscontrol import Role
from src.pwdfile import verify_credential, get_record
from src.enrolment import enrol_user


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
            line = get_record(username, password)
            record = line.strip('\n').split(':')
            role = Role[record[3]]
            if (role == Role['teller'] and ((datetime.now().hour < 8) or (datetime.now().hour > 17))):
                print("Tellers can only access the system during business hours from 9:00AM to 5:00PM.")
            else: 
                login = True
                print(f'> Username: {username}')
                print(f'> Role: {role}')
                print(f'> Permissions: {role.value}')


def user_interface():
    """A basic user interface to prototype the system."""
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


if __name__ == '__main__':
    user_interface()