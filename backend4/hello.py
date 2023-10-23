import os
from flask import Flask
import mysql.connector

server = Flask(__name__)

@server.route('/')
def listBlog():

    return '<div>   backend4  ' + '</div>'
    """
    """
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()

    response = 'backend4'
    for c in rec:
        response = response  + '<div>   backend4  ' + c + '</div>'
    return response


if __name__ == '__main__':
    server.run()
