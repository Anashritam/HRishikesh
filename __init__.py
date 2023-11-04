import sqlite3
import datetime

# Connect to SQLite database
conn = sqlite3.connect("hospital_management.db")
cursor = conn.cursor()

# Create tables (you should create them only once)
# Create tables (you should create them only once)
cursor.execute('''CREATE TABLE IF NOT EXISTS Patients (
                    PatientID INTEGER PRIMARY KEY,
                    FirstName TEXT,
                    LastName TEXT,
                    DateOfBirth DATE,
                    Gender TEXT,
                    ContactNumber TEXT,
                    Address TEXT,
                    InsuranceProvider TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Appointments (
                    AppointmentID INTEGER PRIMARY KEY,
                    PatientID INTEGER,
                    AppointmentDateTime DATETIME,
                    Status TEXT,
                    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
                 )''')


# Function to register a new patient
def register_patient():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    gender = input("Enter gender: ")
    contact_number = input("Enter contact number: ")
    address = input("Enter address: ")
    insurance_provider = input("Enter insurance provider: ")

    cursor.execute('''INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, ContactNumber, Address, InsuranceProvider)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (first_name, last_name, dob, gender, contact_number, address, insurance_provider))

    conn.commit()
    print("Patient registered successfully!")

# Function to schedule an appointment
def schedule_appointment():
    patient_id = int(input("Enter patient ID: "))
    appointment_datetime = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
    status = "Pending"

    cursor.execute('''INSERT INTO Appointments (PatientID, AppointmentDateTime, Status)
                      VALUES (?, ?, ?)''',
                   (patient_id, appointment_datetime, status))

    conn.commit()
    print("Appointment scheduled successfully!")

# Function to display the list of patients
def display_patient_list():
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    if not patients:
        print("No patients found.")
    else:
        print("Patient List:")
        for patient in patients:
            print(f"PatientID: {patient[0]}")
            print(f"First Name: {patient[1]}")
            print(f"Last Name: {patient[2]}")
            print(f"Date of Birth: {patient[3]}")
            print(f"Gender: {patient[4]}")
            print(f"Contact Number: {patient[5]}")
            print(f"Address: {patient[6]}")
            print(f"Insurance Provider: {patient[7]}")
            print("")

# Main menu
while True:
    print("\nHospital Management System")
    print("1. Register Patient")
    print("2. Schedule Appointment")
    print("3. Display Patient List")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()
    elif choice == "2":
        schedule_appointment()
    elif choice == "3":
        display_patient_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
