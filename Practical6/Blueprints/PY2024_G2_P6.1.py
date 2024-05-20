import os
import sqlite3
import re

def create_tables(cursor):
    # Create the Domains table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Domains (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain_name TEXT UNIQUE
    )
    ''')
    
    # Create the Weekdays table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Weekdays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weekday_name TEXT UNIQUE
    )
    ''')
    
    # Create the Emails table with foreign keys referencing Domains and Weekdays
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
    # Function to parse mbox file and extract relevant data
    emails = []
    with open(filename, 'r') as file:
        email = None
        weekday = None
        spam_confidence = None
        for line in file:
            if line.startswith('From '):
                # Extract email and weekday from 'From ' lines
                parts = line.split()
                email = parts[1]
                weekday = parts[2]
            elif line.startswith('X-DSPAM-Confidence:'):
                # Extract spam confidence from 'X-DSPAM-Confidence:' lines
                spam_confidence = float(line.split(':')[1].strip())
                if email and weekday and spam_confidence is not None:
                    emails.append((email, weekday, spam_confidence))
                    # Reset variables for the next email
                    email = None
                    weekday = None
                    spam_confidence = None
    return emails

def insert_data(cursor, emails):
    # Function to insert parsed data into the database tables
    for email, weekday, spam_confidence in emails:
        # Extract domain from email address
        domain = email.split('@')[1]
        
        # Insert domain into Domains table if not already present
        cursor.execute('INSERT OR IGNORE INTO Domains (domain_name) VALUES (?)', (domain,))
        cursor.execute('SELECT id FROM Domains WHERE domain_name=?', (domain,))
        domain_id = cursor.fetchone()[0]
        
        # Insert weekday into Weekdays table if not already present
        cursor.execute('INSERT OR IGNORE INTO Weekdays (weekday_name) VALUES (?)', (weekday,))
        cursor.execute('SELECT id FROM Weekdays WHERE weekday_name=?', (weekday,))
        weekday_id = cursor.fetchone()[0]
        
        # Insert email into Emails table, referencing domain and weekday IDs
        cursor.execute('''
        INSERT OR IGNORE INTO Emails (email_address, domain_id, weekday_id, spam_confidence) 
        VALUES (?, ?, ?, ?)''', (email, domain_id, weekday_id, spam_confidence))

def print_unique_domains(cursor):
    # Function to print and return a list of unique domains
    cursor.execute('SELECT domain_name FROM Domains')
    domains = cursor.fetchall()
    print("Unique domains:")
    for domain in domains:
        print(f"- {domain[0]}")
    return [domain[0] for domain in domains]  # Return a list of domains

def get_emails_by_domain(cursor, domain):
    # Function to retrieve emails by domain
    cursor.execute('''
    SELECT Weekdays.weekday_name, Domains.domain_name, Emails.email_address, Emails.spam_confidence 
    FROM Emails
    JOIN Domains ON Emails.domain_id = Domains.id
    JOIN Weekdays ON Emails.weekday_id = Weekdays.id
    WHERE Domains.domain_name = ?
    ''', (domain,))
    return cursor.fetchall()

def get_emails_on_weekend(cursor):
    # Function to retrieve emails received on Fridays and Saturdays
    cursor.execute('''
    SELECT Weekdays.weekday_name, Domains.domain_name, Emails.email_address, Emails.spam_confidence 
    FROM Emails
    JOIN Domains ON Emails.domain_id = Domains.id
    JOIN Weekdays ON Emails.weekday_id = Weekdays.id
    WHERE Weekdays.weekday_name IN ('Fri', 'Sat')
    ''')
    return cursor.fetchall()

def print_emails(emails):
    # Function to print emails in a nicely formatted manner
    print(f"{'Day':<10}{'Domain':<20}{'Email':<30}{'Spam Confidence'}")
    print("-" * 70)
    for email in emails:
        print(f"{email[0]:<10}{email[1]:<20}{email[2]:<30}{email[3]}")

def main():
    # Print current working directory
    print("Current working directory:", os.getcwd())
    
    # Ensure script uses the directory of the script as the working directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Print current working directory after change
    print("Script directory:", script_dir)
    
    # Connect to SQLite database (creates database if it doesn't exist)
    conn = sqlite3.connect('email_data.db')
    cursor = conn.cursor()
    
    # Create database tables
    create_tables(cursor)
    
    # Parse mbox files and collect email data
    emails = parse_mbox('mbox-short.txt')
    emails.extend(parse_mbox('mbox.txt'))
    
    # Insert email data into database
    insert_data(cursor, emails)
    conn.commit()
    
    # Print unique domains and store the list
    unique_domains = print_unique_domains(cursor)
    
    # Prompt user to enter a domain to filter emails
    domain = input("Enter a domain to filter emails: ")
    if domain not in unique_domains:
        # Print message if the domain is not valid
        print("Please choose a valid domain")
    else:
        # Retrieve and print emails from the specified domain
        emails_by_domain = get_emails_by_domain(cursor, domain)
        print("\nEmails from the domain:", domain)
        print_emails(emails_by_domain)
    
    # Retrieve and print emails received on Fridays and Saturdays
    print("\nEmails received on Fridays and Saturdays:")
    weekend_emails = get_emails_on_weekend(cursor)
    print_emails(weekend_emails)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
