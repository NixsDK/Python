import sqlite3



#Izveidos Domains, Weekdays, Emails
def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Domains (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain_name TEXT UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Weekdays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weekday_name TEXT UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_address TEXT UNIQUE,
        domain_id INTEGER,
        weekday_id INTEGER,
        spam_confidence REAL,
        FOREIGN KEY(domain_id) REFERENCES Domains(id),
        FOREIGN KEY(weekday_id) REFERENCES Weekdays(id)
    )
    ''')


def parse_mbox(filename):
    emails = []
    with open(filename, 'r') as file:
        email = None
        weekday = None
        spam_confidence = None
        for line in file:
            if line.startswith('From '):
                parts = line.split()
                email = parts[1]
                weekday = parts[2]
            elif line.startswith(): #spamconfidence