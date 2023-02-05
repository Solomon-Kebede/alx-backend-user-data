#!/usr/bin/env python3

'''
-User passwords should NEVER be stored in plain text in a database.
-Implement a `hash_password` function that expects one string argument
name `password` and returns a salted, hashed password, which is a byte string.
-Use the `bcrypt` package to perform the hashing (with `hashpw`).
'''

import bcrypt


def hash_password(password: str) -> bytes:
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
    return hashed_password


'''
-Implement an `is_valid` function that expects 2 arguments
and returns a boolean.
-Arguments:
    -`hashed_password`: bytes type
    -`password`: string type
-Use `bcrypt` to validate that the provided password
matches the hashed password.
'''


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Return a boolean if password is the source
    of the hash
    '''
    # converting password to array of bytes
    password_bytes = password.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()
    # checking password
    result = bcrypt.checkpw(password_bytes, hashed_password)
    return result
