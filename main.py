import mysql.connector
import serial
from datetime import datetime
myconn = mysql.connector.connect(host="localhost", user="root", password="Sunbeam@01",
                                 database="school")
cur = myconn.cursor()
serial_port = serial.Serial('COM5', 9600, timeout=1)
def rfid_get():
    try:
        while True:
# Read data from the serial port
            data = serial_port.readline().decode().strip()

# Process the RFID data
            if data:
                return data

    except Exception as e:
        print("error -->" + str(e))


def new(name,reg,rfid_uid):
    cmd = "INSERT INTO user (name, reg_num, rfid_uid,attendance) VALUES ('{}','{}','{}',0)".format(name,reg,rfid_uid)
    cur.execute(cmd)
    myconn.commit()
    print("record updated")

def attendance(rfid_uid):
    cur_date_time = datetime.now()
    cur_date = cur_date_time.day

    cur.execute("SELECT attendance FROM user WHERE rfid_uid = %s", (rfid_uid,))
    current_attendance = cur.fetchone()

    # If there's an existing value, retrieve it; otherwise, initialize an empty string
    if current_attendance:
        current_attendance = current_attendance[0]
    else:
        current_attendance = ''

    # Concatenate the new value with the existing value
    new_attendance = current_attendance + ' ' + str(cur_date)  # Modify this concatenation as needed
    # Update the attendance column with the new concatenated value for the specified rfid_uid
    cur.execute("UPDATE user SET attendance = %s WHERE rfid_uid = %s", (new_attendance, rfid_uid))

    # Commit the changes to the database
    myconn.commit()
    print("Success , Attendance recorded for the rfid_uid -> " + str(cur_date))


while True:

    print("Enter 1 to input new user info")
    print("Enter 2 for checking attendance of existing user")
    op=int(input())
    if(op==1):
        print("Enter user name:")
        name=input()
        print("Enter reg_no:")
        reg=input()
        rfid_uid = rfid_get()
        new(name,reg,rfid_uid)



        print("User info inserted successfully!")
    elif(op==2):
        print("Scan the Rfid")
        rfid_uid = rfid_get()
        print(rfid_uid)
        attendance(rfid_uid)



    else:
        print("Invalid option")


