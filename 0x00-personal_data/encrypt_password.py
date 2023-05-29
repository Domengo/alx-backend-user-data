#!/usr/bin/env python3
"""encrypt pswd
"""
import bcrypt


def hash_password(password):
    """encrypt pswd
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# bytes = password.encode('utf-8')

# # generating the salt
# salt = bcrypt.gensalt()

# # Hashing the password
# hash = bcrypt.hashpw(bytes, salt)
