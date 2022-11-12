import string
import time
import unittest
import random

# random password function
# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*?_")


def generate_random_password():
    # length of password
    length = random.randint(15, 32)

    # shuffle the characters
    random.shuffle(characters)

    # pick random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # shuffle the resultant password
    random.shuffle(password)

    # convert the list to string
    return ("".join(password))


# assign variable to function and print the example
password = generate_random_password()
print(password)