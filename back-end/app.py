from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import os

app = Flask(__name__)


def createDatabase():
    conn = sqlite3.connect("educompDB.db")
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS COMPLAINT(
                    FROM_NAME TEXT,
                    TO_NAME TEXT,
                    DESC TEXT,
                    STATUS TEXT,
                    COMPLAINT_ID INTEGER,
                    UNIQUE (COMPLAINT_ID),
                    PRIMARY KEY(COMPLAINT_ID)
                );
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS ADMINISTRATOR(
                    USERNAME TEXT,
                    PASSWORD TEXT,
                    USER_TYPE TEXT,
                    COMPLAINT_ID INTEGER,
                    FOREIGN KEY(COMPLAINT_ID) REFERENCES COMPLAINT(COMPLAINT_ID)
                );
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS FACULTY(
                    NAME TEXT,
                    STAFF_ID TEXT,
                    DESIGNATION TEXT,
                    PHONE_NUMBER INTEGER,
                    COMPLAINT_ID INTEGER,
                    FOREIGN KEY(COMPLAINT_ID) REFERENCES COMPLAINT(COMPLAINT_ID)
                );
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS STUDENT(
                    NAME TEXT,
                    USN TEXT,
                    YEAR INTEGER,
                    PHONE_NUMBER INTEGER,
                    COMPLAINT_ID INTEGER,
                    FOREIGN KEY(COMPLAINT_ID) REFERENCES COMPLAINT(COMPLAINT_ID)
                );
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS PARENT(
                    NAME TEXT,
                    CHILD TEXT,
                    PHONE_NUMBER INTEGER,
                    COMPLAINT_ID INTEGER,
                    FOREIGN KEY(COMPLAINT_ID) REFERENCES COMPLAINT(COMPLAINT_ID)
                );
                """)
    

    conn.commit()

    
if __name__ == "__main__":
    if not os.path.exists("educompDB.db"):
        createDatabase()
    app.run(debug=True)