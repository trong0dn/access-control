### enrolment mechanism and the proactive password checker
import getpass
import re
from src.accesscontrol import Role
from src.pwdfile import create_record


SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '?', '*']
BLOCKLIST = "etc/blocklist.txt"


def enrol_user() -> None:
    """Enrol user to the system.

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
                print("CREDENTIAL ACCEPTED")
            else:
                print("CREDENTIAL DENIED")
        
        valid_role = False
        while (not valid_role):
            print([member.name for member in Role])
            role = input("Select role: ")
            if role in Role.__members__:
                valid_role = True
                print("ROLE ACCEPTED")
            else:
                print("ROLE INVALID")
        
        if (valid_credentials and valid_role):
            create_record(username, password, Role[role])
            enrol = True
            print("ENROL SUCCESS")


def password_policy(username: str, password: str) -> bool:
    """Describes the password policy.

    Parameters:
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
        not (password == username) # matching the user ID must be prohibited
    ):
        if (
            not (re.search("^\d{4}-\d{2}-\d{2}$", password)) and # format of calendar dates prohibited
            not (re.search("^[A-Z0-9]{7}$", password)) and  # format of license plate numbers prohibited
            not (re.search("^\d{3}-\d{3}-\d{4}$", password)) and  # format of telephone numbers prohibited
            not (re.search("^\d{1-12}$", password)) # common numbers must be prohibited
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

    Parameters:
        password (str): The plaintext of the disallowed password.

    Returns:
        bool: True if the password was added to the blocklist, otherwise False. 
   """
    with open(BLOCKLIST, 'r+') as file:
        blocklist = file.read()
        file.close()
        if password in blocklist: # common weak passwords must be prohibited
            return False
        else:
            file.write(password)
            return True
        

if __name__ == '__main__':
    print(add_disallowed_password("Qwerty123"))