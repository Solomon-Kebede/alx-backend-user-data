#!/usr/bin/env python3
""" Module for handling views of Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - Authenticate user credentials for login
    """
    # all_users = [user.to_json() for user in User.all()]
    # return jsonify(all_users)
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None:
        return jsonify({ "error": "email missing" }), 400
    if password is None:
        return jsonify({ "error": "password missing" }), 400
    users = User.search({"email": email})
    if users == []:
        return jsonify({ "error": "no user found for this email" }), 404
    for user in users:
        user_validity = user.is_valid_password(password)
        if not user_validity:
            return jsonify({ "error": "wrong password" }), 401
        elif user_validity:
            from api.v1.app import auth
            user_id = user.__dict__.get("id")
            # print(user_id)
            session_id = auth.create_session(user_id)
            cookie_name = os.getenv("SESSION_NAME")
            # return jsonify(user.to_json()), 200
            # out = jsonify(state=0, msg='success')
            out = jsonify(user.to_json())
            out.set_cookie(cookie_name, session_id)
            return out, 200
    # print(f"{email}:{password}")
    # return None