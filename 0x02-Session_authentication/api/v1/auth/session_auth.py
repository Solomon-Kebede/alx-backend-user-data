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
            return session_id
