import sqlite3
import random

conn = sqlite3.connect('telekom_data.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Call_Logs')
cursor.execute('DROP TABLE IF EXISTS Customers')

cursor.execute('''
CREATE TABLE Customers (
    Customer_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Contract_Type TEXT,
    Monthly_Fee INTEGER,
    Loyalty_End_Date TEXT
)
''')

cursor.execute('''
CREATE TABLE Call_Logs (
    Log_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_ID INTEGER,
    Complaint_Text TEXT,
    Call_Duration_Min INTEGER,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
)
''')

contracts = ['GigaNet Pro', 'Mobile S', 'Mobile XL', 'TV + Net Combo']
complaints = [
    "The internet is super fast, I am very satisfied!",
    "The wifi keeps disconnecting, terrible service, I want to cancel!",
    "I have a question about my latest bill, I don't understand the amount.",
    "Mobile internet is slow in the city center, what can you do?",
    "Everything is fine, I just want to change my package.",
    "It's outrageous that there has been no TV broadcast for days!",
    "The agent was very kind, thank you for the quick help."
]

first_names = ["Gabor", "Anna", "Peter", "Zita", "Laszlo", "Janos", "Eszter", "Bence"]
last_names = ["Kovacs", "Nagy", "Toth", "Szabo", "Horvath", "Varga", "Kiss", "Molnar"]

for i in range(1, 101):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    contract = random.choice(contracts)
    fee = random.randint(5000, 15000)
    
    cursor.execute("INSERT INTO Customers (Customer_ID, Name, Contract_Type, Monthly_Fee, Loyalty_End_Date) VALUES (?, ?, ?, ?, '2026-12-31')", 
                   (i, name, contract, fee))
    
    call_count = random.randint(1, 3)
    for _ in range(call_count):
        complaint = random.choice(complaints)
        duration = random.randint(2, 25)
        cursor.execute("INSERT INTO Call_Logs (Customer_ID, Complaint_Text, Call_Duration_Min) VALUES (?, ?, ?)", 
                       (i, complaint, duration))

conn.commit()
conn.close()

print("Success! Database and 100 rows generated.")