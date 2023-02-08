#!/usr/bin/env python3
"""
Module for Basic Authentication
"""
from api.v1.auth.auth import Auth


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
