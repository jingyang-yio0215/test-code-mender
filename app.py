import sqlite3
import subprocess


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM users WHERE name = ?"
    return conn.execute(query, (username,)).fetchall()


def ping(host):
    return subprocess.run(["ping", "-c", "1", host], capture_output=True)
