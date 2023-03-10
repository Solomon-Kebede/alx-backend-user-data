#!/usr/bin/env python3
"""
Module for Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """docstring for BasicAuth"""
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """Extract base64 text from header"""
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header[0:6] == "Basic ":
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """Decode extracted base64 value"""
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        else:
            try:
                return base64.b64decode(
                    base64_authorization_header
                ).decode("utf-8")
            except Exception as e:
                return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None
        elif ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """Returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        elif user_pwd is None or not isinstance(user_pwd, str):
            return None
        else:
            # import pprint
            # pprint.pprint(User.__dict__)
            try:
                users = User.search({"email": user_email})
            except Exception:
                return None
            if users == []:
                return None
            else:
                for user in users:
                    user_validity = user.is_valid_password(user_pwd)
                    if user_validity:
                        return user
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request"""
        # print(request)
        auth_header = self.authorization_header(request)
        # print(auth_header)
        auth_header_extracted = self.extract_base64_authorization_header(
            auth_header
        )
        # print(auth_header_extracted)
        decoded_auth_header = self.decode_base64_authorization_header(
            auth_header_extracted
        )
        # print(decoded_auth_header)
        extracted_credentials = self.extract_user_credentials(
            decoded_auth_header
        )
        # print(extracted_credentials)
        user_object = self.user_object_from_credentials(*extracted_credentials)
        # print(user_object.__dict__)
        return user_object
