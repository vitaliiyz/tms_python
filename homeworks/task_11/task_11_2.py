import re


def email_validation(email: str):
    if "@" in email and email.count("@") == 1:
        username, hostname = email.split("@")
        print(bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', email)))
    else:
        print("Email is incorrect")


email_validation("vz260198@gmail.com")
