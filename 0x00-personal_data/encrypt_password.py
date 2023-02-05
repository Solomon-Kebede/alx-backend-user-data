#!/usr/bin/env python3

'''
-User passwords should NEVER be stored in plain text in a database.
-Implement a `hash_password` function that expects one string argument
name `password` and returns a salted, hashed password, which is a byte string.
-Use the `bcrypt` package to perform the hashing (with `hashpw`).
'''

import bycrypt


def hash_password(password):
    '''
    Return a salted, hashed password, which is a
    byte string using bycrypt.hashpw
    '''
    # converting password to array of bytes
    password_bytes = password.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    print(hashed_password)
