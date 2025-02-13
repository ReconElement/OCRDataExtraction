import sqlite3
con = sqlite3.connect("medical_records.db")
cur = con.cursor()
#create the required tables in sqlitedb "medical.db"

cur.execute("""CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob DATE
);
""")

cur.execute("""
CREATE TABLE forms_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    form_json TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
 """)

