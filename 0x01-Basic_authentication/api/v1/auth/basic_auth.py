#!/usr/bin/env python3
"""
Module for Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64


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
