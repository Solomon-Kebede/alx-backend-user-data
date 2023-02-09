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
        test1 = (path in excluded_paths)
        test2 = (f"{path}/" in excluded_paths)
        test3 = (path[0:-1] in excluded_paths)
        if test1 or test2 or test3:
            return False
        elif not test1 or not test2 or not test3:
            return True

    def authorization_header(self, request=None) -> str:
        """docstrings for authorization_header"""
        if request is None:
            return None
        elif 'HTTP_AUTHORIZATION' not in request.__dict__.get('environ'):
            return None
        elif 'HTTP_AUTHORIZATION' in request.__dict__.get('environ'):
            return request.__dict__.get('environ').get('HTTP_AUTHORIZATION')

    def current_user(self, request=None) -> TypeVar('User'):
        """docstrings for current_user"""
        return None
