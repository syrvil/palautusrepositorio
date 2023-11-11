import re
import sys, pdb
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        # debug
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
 
        elif len(username) < 3:
            raise UserInputError("Username must have at least 3 characters")
        elif re.match("^[a-z]+$", username) is None:
            raise UserInputError("Username must only contain letters a-z")
        elif len(password) < 8:
            raise UserInputError("Password must have at least 8 characters")
        elif re.match("^[a-z]+$", password) is not None:
            raise UserInputError("Password cannot contain olnly letters")

        