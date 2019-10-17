#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, redirect, url_for, escape, request, jsonify
from uuid import uuid4
app = Flask(__name__)

# TODO: добавить postgresql , redis для сессий
session_data: dict = dict()


def get_tm() -> int:
    return 60 * 60 * 1000


@app.route('/login', methods=["POST"])
def login():

    json_data: dict = request.json
    login: str = json_data.get("login")
    password: str = json_data.get("password")

    if login in session_data:
        if password == session_data[login]["password"]:
            if session_data[login]["session"]:
                session_uuid: str = session_data[login]["session"]
            else:
                session_uuid: str = str(uuid4())
            return jsonify({"session": session_uuid, "status": 200, "tm": get_tm()})
        else:
            return jsonify({"message": "Wrong password", "status": 500})
    else:
        return jsonify({"message": "Not found login", "status": 500})


@app.route("/registration", methods=["POST"])
def registration():

    json_data: dict = request.json
    login: str = json_data.get("login")
    password: str = json_data.get("password")

    if login in session_data:
        return jsonify({"message": "A user with such login is already there", "status": 500})
    else:
        session_uuid: str = str(uuid4())
        session_data[login] = {"login": login, "password": password, "session": session_uuid, "tm": get_tm()}
        return jsonify({"session": session_uuid, "status": 200, "tm": get_tm()})


@app.route('/logout', methods=["POST"])
def logout():
    # remove the username from the session if its there
    json_data: dict = request.json
    session = json_data.get("session")
    print(json_data)
    return jsonify({"status": 200})


@app.route('/changepassword', methods=["POST"])
def changepassword():
    json_data: dict = request.json
    session = json_data.get("session")
    new_pass: str = json_data.get("newPass")
    old_pass: str = json_data.get("oldPass")

    for k, v in session_data.items():
        if v.get("session") == session:
            if v.get("password") == old_pass:
                v["password"] = new_pass
                return jsonify({"status": 200})

    print(json_data)
    return jsonify({"status": 500})

# set the secret key.  keep this really secret:
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    print("Start: Api")
    app.run(debug=True, host="0.0.0.0", port=5000)
    print("end: Api")
