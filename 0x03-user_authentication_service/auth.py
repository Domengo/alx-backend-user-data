#!/usr/bin/env python3
"""
a _hash_password method that takes in a password string arguments
and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments
    and returns bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password.

        Args:
            email (str): The email of the new user.
            password (str): The password of the new user.

        Returns:
            User: The User object for the new user.

        Raises:
            ValueError:
                If a user with the same email already exists in the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
        raise ValueError(f'User {email} already exists.')