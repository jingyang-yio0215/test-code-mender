import sqlite3
import subprocess


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    # Intentionally vulnerable (SQL injection) to test CodeMender
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return conn.execute(query).fetchall()


def ping(host):
    return subprocess.run(["ping", "-c", "1", host], capture_output=True)
