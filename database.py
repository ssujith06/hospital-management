import sqlite3

# Create Database Connection
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    age INTEGER, 
    date_of_visit TEXT, 
    diagnosis TEXT, 
    treatment TEXT, 
    doctor TEXT
)
""")

conn.commit()

# Functions for Database Operations
def add_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def check_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone()

def add_patient(name, age, date_of_visit, diagnosis, treatment, doctor):
    cursor.execute("INSERT INTO patients (name, age, date_of_visit, diagnosis, treatment, doctor) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, age, date_of_visit, diagnosis, treatment, doctor))
    conn.commit()

def get_patients():
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()
