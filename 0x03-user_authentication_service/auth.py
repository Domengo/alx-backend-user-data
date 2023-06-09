#!/usr/bin/env python3
"""
a _hash_password method that takes in a password string arguments
and returns bytes.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments
    and returns bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
