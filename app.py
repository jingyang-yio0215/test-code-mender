import sqlite3
import subprocess


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    # Intentionally vulnerable (SQL injection) to test CodeMender
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return conn.execute(query).fetchall()


def ping(host):
    # Intentionally vulnerable (command injection) to test CodeMender
    return subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
