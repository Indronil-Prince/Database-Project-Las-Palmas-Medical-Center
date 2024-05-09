import mysql.connector
import sys

def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="2489",
        database="project"
    )

def query_1(proc_name):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Physician.* FROM Physician "
            "INNER JOIN Undergoes ON Physician.physicianID = Undergoes.physicianID "
            "INNER JOIN `Procedure` ON Undergoes.procedureID = `Procedure`.procID "
            "WHERE `Procedure`.name = %s"
        )
        cursor.execute(query, (proc_name,))
        for result in cursor:
            print("physicianID: {}, name: {}, position: {}, ssn: {}".format(
                result['physicianID'], result['name'], result['position'], result['ssn']
            ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
        
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_2():

    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Patient.name AS patient_name, Physician.name AS physician_name, Nurse.name AS nurse_name, "
            "Appointment.startDateTime, Appointment.endDateTime, PhysicianHead.name AS primary_physician "
            "FROM Appointment "
            "INNER JOIN Patient ON Appointment.patientID = Patient.patientID "
            "INNER JOIN Physician ON Appointment.physicianID = Physician.physicianID "
            "INNER JOIN Nurse ON Appointment.nurseID = Nurse.nurseID "
            "INNER JOIN Physician AS PhysicianHead ON Patient.primaryPhysID = PhysicianHead.physicianID "
            "WHERE Appointment.physicianID != Patient.primaryPhysID"
        )
        cursor.execute(query)
        for result in cursor:
            print("patient_name: {}, physician_name: {}, nurse_name: {}, "
                  "start_datetime: {}, end_datetime: {}, primary_physician: {}".format(
                      result['patient_name'], result['physician_name'], result['nurse_name'],
                      result['startDateTime'], result['endDateTime'], result['primary_physician']
                  ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_3(given_cost):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT * FROM Patient "
            "INNER JOIN Undergoes ON Patient.patientID = Undergoes.patientID "
            "INNER JOIN `Procedure` ON Undergoes.procedureID = `Procedure`.procID "
            "WHERE `Procedure`.cost > %s"
        )
        cursor.execute(query, (given_cost,))
        for result in cursor:
            print("patientID: {}, ssn: {}, name: {}, address: {}, dob: {}, phone: {}, insuranceNumber: {}, primaryPhysID: {}".format(
                result['patientID'], result['ssn'], result['name'], result['address'], result['dob'], result['phone'],
                result['insuranceNumber'], result['primaryPhysID']
            ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_4(department_name):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Patient.* FROM Patient "
            "INNER JOIN Physician ON Patient.primaryPhysID = Physician.physicianID "
            "INNER JOIN Department ON Physician.physicianID = Department.headID AND Department.headID = Physician.physicianID "
            "WHERE Department.name = %s"
        )
        cursor.execute(query, (department_name,))
        for result in cursor:
            print("patientID: {}, ssn: {}, name: {}, address: {}, dob: {}, phone: {}, insuranceNumber: {}, primaryPhysID: {}".format(
                result['patientID'], result['ssn'], result['name'], result['address'], result['dob'], result['phone'],
                result['insuranceNumber'], result['primaryPhysID']
            ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_5(medication_name):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Patient.name AS patient_name, Physician.name AS physician_name, Prescribes.prescribedDate "
            "FROM Prescribes "
            "INNER JOIN Patient ON Prescribes.patientID = Patient.patientID "
            "INNER JOIN Physician ON Prescribes.physicianID = Physician.physicianID "
            "INNER JOIN Medication ON Prescribes.medicationID = Medication.medID "
            "WHERE Medication.name = %s"
        )
        cursor.execute(query, (medication_name,))
        for result in cursor:
            print("patient_name: {}, physician_name: {}, prescribed_date: {}".format(
                result['patient_name'], result['physician_name'], result['prescribedDate']
            ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_6(date):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Nurse.*, OnCall.startDate on_call_start_date, onCall.endDate on_call_end_date FROM Nurse "
            "INNER JOIN OnCall ON Nurse.nurseID = OnCall.nurseID "
            "WHERE %s BETWEEN OnCall.startDate AND OnCall.endDate"
        )
        cursor.execute(query, (date,))
        for result in cursor:
            print("nurseID: {}, name: {}, position: {}, ssn: {}, on_call_start_date: {}, on_call_end_date: {}".format(
                result['nurseID'], result['name'], result['position'], result['ssn'], result['on_call_start_date'], result['on_call_end_date']
            ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_7(date):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Stay.roomID, Patient.name AS patient_name, Stay.startDate, Stay.endDate "
            "FROM Stay "
            "INNER JOIN Patient ON Stay.patientID = Patient.patientID "
            "INNER JOIN Room ON Stay.roomID = Room.roomID "
            "WHERE Room.roomType = 'Double' AND %s BETWEEN Stay.startDate AND Stay.endDate"
        )
        cursor.execute(query, (date,))
        current_room_id = None
        for result in cursor:
            if result['roomID'] != current_room_id:
                print("Room ID: {}".format(result['roomID']))
                current_room_id = result['roomID']
            print("\tPatient: {}, Stay Start Date: {}, Stay End Date: {}".format(
                result['patient_name'], result['startDate'], result['endDate']
            ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

def query_8(department_name):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = (
            "SELECT Patient.patientID, Patient.ssn as patient_ssn, Patient.name as patient_name, Patient.address as patient_address, Patient.dob as patient_dob,"
            "Patient.phone as patient_phone, Patient.insuranceNumber as patient_insuranceNumber, Patient.primaryPhysID as patient_primaryPhysID,"
            "Physician.*, Appointment.appID "
            "FROM Appointment "
            "INNER JOIN Patient ON Appointment.patientID = Patient.patientID "
            "INNER JOIN Physician ON Appointment.physicianID = Physician.physicianID "
            "INNER JOIN AffiliatedWith ON Physician.physicianID = AffiliatedWith.physicianID "
            "INNER JOIN Department ON AffiliatedWith.departmentID = Department.deptID "
            "WHERE Department.name = %s"
        )
        cursor.execute(query, (department_name,))
        for result in cursor:
            print("patientID: {}, patient_ssn: {}, patient_name: {}, patient_address: {}, patient_dob: {}, "
                  "patient_phone: {}, patient_insuranceNumber: {}, patient_primaryPhysID: {}, "
                  "physicianID: {}, physician_name: {}, physician_position: {}, physician_ssn: {}, "
                  "appointmentID: {}".format(
                      result['patientID'], result['patient_ssn'], result['patient_name'], result['patient_address'], result['patient_dob'],
                      result['patient_phone'], result['patient_insuranceNumber'], result['patient_primaryPhysID'], result['physicianID'], 
                      result['name'], result['position'], result['ssn'], result['appID']
                  ))
        row = cursor.rowcount
        if row < 1:
            print("No such data found!")
    except mysql.connector.Error as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    command = sys.argv[1]
    if command == '1':
        query_1(sys.argv[2])
    elif command == '2':
        query_2()
    elif command == '3':
        query_3(float(sys.argv[2]))
    elif command == '4':
        query_4(sys.argv[2])
    elif command == '5':
        query_5(sys.argv[2])
    elif command == '6':
        query_6(sys.argv[2])
    elif command == '7':
        query_7(sys.argv[2])
    elif command == '8':
        query_8(sys.argv[2])
    else:
        print("Invalid command.")
