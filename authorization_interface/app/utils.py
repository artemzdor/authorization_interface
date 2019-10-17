#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
import psycopg2
from typing import List, Tuple
from psycopg2._psycopg import connection, cursor

import config_init

TABLE_NAME: str = 'users'

CREATE_TABLE: str = """
CREATE TABLE {table_name}
(
    id bigserial NOT NULL,
    login text NOT NULL,
    password text NOT NULL,
    removed boolean NOT NULL,
    tm_create timestamp with time zone NOT NULL DEFAULT now(),
    tm_removed timestamp with time zone,
    PRIMARY KEY (id)
)
""".format(table_name=TABLE_NAME)


INSERT_USER_DATA: str = """
INSERT INTO {table_name} (login, password, removed) 
VALUES ('{login}'::text, '{password}'::text, false::boolean)
returning id;
"""


UPDATE_BOOK: str = """
UPDATE {table_name} 
SET password = {password}::text 
WHERE id = {id_user};
"""


def get_table_name() -> str:
    return TABLE_NAME


def get_connect_ps() -> connection:
    config_connect: dict = config_init.load_config()
    pg_con: connection = psycopg2.connect(**config_connect["pg_connect"])
    return pg_con


def create_table(table_name: str, conn: connection) -> None:
    cur: cursor = conn.cursor()
    cur.execute(CREATE_TABLE)
    conn.commit()


def check_table(table_name: str, conn: connection) -> bool:
    cur: cursor = conn.cursor()
    try:
        cur.execute(f"select * from {table_name} where false;")
        row = cur.fetchone()
        conn.rollback()
        return True
    except Exception as e:
        conn.rollback()
        return False


conn: connection = get_connect_ps()

if check_table("users", conn=conn):
    print("Pass table")
else:
    print("Create table")
    create_table("users", conn=conn)

cur: cursor = conn.cursor()
sql: str = INSERT_USER_DATA.format(table_name=get_table_name(), login="u1", password="passwords")
id_user: int = cur.execute(query=sql)
row = cur.fetchone()
conn.commit()
row = cur.fetchone()
print()

