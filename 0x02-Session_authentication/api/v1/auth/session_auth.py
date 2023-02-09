#!/usr/bin/env python3
"""
Module for Session Authentication
"""
from api.v1.auth.auth import Auth
from uuid import uuid4 as id


class SessionAuth(Auth):
    """docstring for SessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        elif not isinstance(user_id, str):
            return None
        else:
            session_id = id()
            self.user_id_by_session_id[str(session_id)] = user_id
            return str(session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        elif not isinstance(session_id, str):
            return None
        else:
            return self.user_id_by_session_id.get(session_id)
