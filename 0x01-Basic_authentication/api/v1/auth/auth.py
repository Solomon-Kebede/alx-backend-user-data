#!/usr/bin/env python3
"""
Module for Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """docstrings for Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """docstrings for require_auth"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path not in excluded_paths:
            return True
        elif path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """docstrings for authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """docstrings for current_user"""
        return None
