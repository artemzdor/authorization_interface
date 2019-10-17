#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, redirect, url_for, escape, request, jsonify
from uuid import uuid4
app = Flask(__name__)

session: dict = dict()


def get_tm() -> int:
    return 60 * 60 * 1000


@app.route('/login', methods=["POST"])
def login():

    json_regis: dict = request.json
    login: str = json_regis.get("login")
    password: str = json_regis.get("password")

    if login in session:
        if password == session[login]["password"]:
            if session[login]["session"]:
                session_uuid: str = session[login]["session"]
            else:
                session_uuid: str = str(uuid4())
            return jsonify({"session": session_uuid, "status": 200, "tm": get_tm()})
        else:
            return jsonify({"message": "Wrong password", "status": 500})
    else:
        return jsonify({"message": "Not found login", "status": 500})


@app.route("/registration", methods=["POST"])
def registration():

    json_regis: dict = request.json
    login: str = json_regis.get("login")
    password: str = json_regis.get("password")

    if login in session:
        return jsonify({"message": "A user with such login is already there", "status": 500})
    else:
        session_uuid: str = str(uuid4())
        session[login] = {"login": login, "password": password, "session": session_uuid, "tm": get_tm()}
        return jsonify({"session": session_uuid, "status": 200, "tm": get_tm()})


@app.route('/logout', methods=["POST"])
def logout():
    # remove the username from the session if its there
    session.pop('username', None)
    return jsonify({{"status": 200}})


@app.route('/changepassword', methods=["POST"])
def logout1():
    json_regis: dict = request.json
    login: str = json_regis.get("login")
    password: str = json_regis.get("password")

    session.pop('username', None)
    return jsonify({{"status": 200}})

# set the secret key.  keep this really secret:
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    print("Start: Api")
    app.run(debug=True, host="0.0.0.0", port=5000)
    print("end: Api")
