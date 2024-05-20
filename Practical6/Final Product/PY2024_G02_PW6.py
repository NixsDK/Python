import os
import sqlite3

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
            elif line.startswith('X-DSPAM-Confidence:'):
                spam_confidence = float(line.split(':')[1].strip())
                if email and weekday and spam_confidence is not None:
                    emails.append((email, weekday, spam_confidence))
    return emails

def insert_data(cursor, emails):
    for email, weekday, spam_confidence in emails:
        domain = email.split('@')[1]

        cursor.execute('INSERT OR IGNORE INTO Domains (domain_name) VALUES (?)', (domain,))
        cursor.execute('SELECT id FROM Domains WHERE domain_name=?', (domain,))
        domain_id = cursor.fetchone()[0]
        
        cursor.execute('INSERT OR IGNORE INTO Weekdays (weekday_name) VALUES (?)', (weekday,))
        cursor.execute('SELECT id FROM Weekdays WHERE weekday_name=?', (weekday,))
        weekday_id = cursor.fetchone()[0]
        
        cursor.execute('''
        INSERT OR IGNORE INTO Emails (email_address, domain_id, weekday_id, spam_confidence) 
        VALUES (?, ?, ?, ?)''', (email, domain_id, weekday_id, spam_confidence))

def print_unique_domains(cursor):
    cursor.execute('SELECT domain_name FROM Domains')
    domains = cursor.fetchall()
    print("Unique domains:")
    for domain in domains:
        print(f"- {domain[0]}")
    return [domain[0] for domain in domains]

def get_emails_by_domain(cursor, domain):
    cursor.execute('''
    SELECT Weekdays.weekday_name, Domains.domain_name, Emails.email_address, Emails.spam_confidence 
    FROM Emails
    JOIN Domains ON Emails.domain_id = Domains.id
    JOIN Weekdays ON Emails.weekday_id = Weekdays.id
    WHERE Domains.domain_name = ?
    ''', (domain,))
    return cursor.fetchall()

def get_emails_on_weekend(cursor):
    cursor.execute('''
    SELECT Weekdays.weekday_name, Domains.domain_name, Emails.email_address, Emails.spam_confidence 
    FROM Emails
    JOIN Domains ON Emails.domain_id = Domains.id
    JOIN Weekdays ON Emails.weekday_id = Weekdays.id
    WHERE Weekdays.weekday_name IN ('Fri', 'Sat')
    ''')
    return cursor.fetchall()

def print_emails(emails):
    print(f"{'Day':<10}{'Domain':<20}{'Email':<30}{'Spam Confidence'}")
    print("-" * 70)
    for email in emails:
        print(f"{email[0]:<10}{email[1]:<20}{email[2]:<30}{email[3]}")

def main():
    #print("Current working directory:", os.getcwd())
    
    #script_dir = os.path.dirname(os.path.abspath(__file__))
    #os.chdir(script_dir)
    
    #print("Script directory:", script_dir)
    
    conn = sqlite3.connect('email_data.db')
    cursor = conn.cursor()
    
    create_tables(cursor)
    
    emails = parse_mbox('mbox-short.txt')
    emails.extend(parse_mbox('mbox.txt'))
    
    insert_data(cursor, emails)
    conn.commit()
    
    running = True
    
    while running:
        
        print("\nChoose option: ")
        print("1. Filter Emails by domain name")
        print("2. Print emails recieved on Saturday and Friday")
        print("3. Exit")
        choice = input("Your choice -> ")
        
        if choice == "1":
            unique_domains = print_unique_domains(cursor)
            domain = input("Enter a domain to filter emails: ")
            if domain not in unique_domains:
                print("Please choose a valid domain")
            else:
                emails_by_domain = get_emails_by_domain(cursor, domain)
                print("\nEmails from the domain:", domain)
                print_emails(emails_by_domain)
                continue
        elif choice == "2":
    
            print("\nEmails received on Fridays and Saturdays:")
            weekend_emails = get_emails_on_weekend(cursor)
            print_emails(weekend_emails)
        elif choice == "3":
            running = False
        else:
            print("Please choose one of the three options")
    
    conn.close()

main()
