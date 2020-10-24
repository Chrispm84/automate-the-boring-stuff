#! python3

import re

def check_password():
    if len(mo) >= 8:
        print("Password is long enough...")
        if len(mo1) >= 1:
            print("Password has at least 1 capital character...")
            if len(mo2) >= 1:
                print("Password has at least 1 lower case character...")
                if len(mo3) >= 1:
                    print("Password has at least 1 digit...")
                    if len(mo4) >= 1:
                        print("Password even has a special character! \nPassword Strength: Goku!")
                    else:
                        print("Password could use special characters. \nPassword Strength: Vegeta!")
                else:
                    print("Password needs at least 1 digit! \nPassword Strength: Weak...")
            else:
                print("Password needs at least one lower case character! \nPassword Strength: Depressing...")
        else:
            print("Password needs at least one capital character! \nPassword Strength: Depressing...")
    else:
        print("Password is too short! \nPassword Strength: Pathetic...")

password = input("Enter your password to test it's strength!\n")

password_regex_length = re.compile(r'[a-zA-Z0-9~!@#$%^&*]')
password_regex_caps = re.compile(r'[A-Z]')
password_regex_lower = re.compile(r'[a-z]')
password_regex_digit = re.compile(r'[0-9]')
password_regex_special = re.compile(r'[~!@#$%^&*]')

mo = password_regex_length.findall(password)
mo1 = password_regex_caps.findall(password)
mo2 = password_regex_lower.findall(password)
mo3 = password_regex_digit.findall(password)
mo4 = password_regex_special.findall(password)

# print(mo)
# print(mo1)
# print(mo2)
# print(mo3)
# print(mo4)

check_password()