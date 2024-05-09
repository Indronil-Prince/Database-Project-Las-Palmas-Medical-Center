-- Create Physician table
CREATE TABLE Physician (
    physicianID INT PRIMARY KEY,
    name VARCHAR(40),
    position VARCHAR(40) CHECK (position IN ('Intern', 'Surgeon', 'Senior', 'Chief of Medicine', 'Resident', 'Psychiatrist')),
    ssn INT UNIQUE
);

-- Create Department table
CREATE TABLE Department (
    deptID INT PRIMARY KEY,
    name VARCHAR(40) CHECK (name IN ('General Medicine', 'Surgery', 'Psychiatry')),
    headID INT,
    FOREIGN KEY (headID) REFERENCES Physician(physicianID)
);

-- Create AffiliatedWith table
CREATE TABLE AffiliatedWith (
    physicianID INT,
    departmentID INT,
    PRIMARY KEY (physicianID, departmentID),
    FOREIGN KEY (physicianID) REFERENCES Physician(physicianID),
    FOREIGN KEY (departmentID) REFERENCES Department(deptID)
);

-- Create Procedure table
CREATE TABLE `Procedure` (
    procID INT PRIMARY KEY,
    name VARCHAR(40),
    cost REAL
);

-- Create Patient table
CREATE TABLE Patient (
    patientID INT PRIMARY KEY,
    ssn INT UNIQUE,
    name VARCHAR(40),
    address VARCHAR(100),
    dob DATE,
    phone VARCHAR(16),
    insuranceNumber INT,
    primaryPhysID INT,
    FOREIGN KEY (primaryPhysID) REFERENCES Physician(physicianID)
);

-- Create Nurse table
CREATE TABLE Nurse (
    nurseID INT PRIMARY KEY,
    name VARCHAR(40),
    position VARCHAR(40) CHECK (position IN ('Head Nurse', 'Nurse')),
    ssn INT UNIQUE
);

-- Create Medication table
CREATE TABLE Medication (
    medID INT PRIMARY KEY,
    name VARCHAR(40)
);

-- Create Prescribes table
CREATE TABLE Prescribes (
    physicianID INT,
    patientID INT,
    medicationID INT,
    prescribedDate DATE,
    dose VARCHAR(40),
    PRIMARY KEY (physicianID, patientID, medicationID),
    FOREIGN KEY (physicianID) REFERENCES Physician(physicianID),
    FOREIGN KEY (patientID) REFERENCES Patient(patientID),
    FOREIGN KEY (medicationID) REFERENCES Medication(medID)
);

-- Create Room table
CREATE TABLE Room (
    roomID INT PRIMARY KEY,
    roomType VARCHAR(40) CHECK (roomType IN ('Single', 'Double'))
);

-- Create Stay table
CREATE TABLE Stay (
    stayID INT PRIMARY KEY,
    patientID INT,
    roomID INT,
    startDate DATE,
    endDate DATE,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID),
    FOREIGN KEY (roomID) REFERENCES Room(roomID)
);

-- Create Undergoes table
CREATE TABLE Undergoes (
    patientID INT,
    procedureID INT,
    stayID INT,
    procDate DATE,
    physicianID INT,
    nurseID INT,
    PRIMARY KEY (patientID, procedureID, stayID),
    FOREIGN KEY (patientID) REFERENCES Patient(patientID),
    FOREIGN KEY (procedureID) REFERENCES `Procedure`(procID),
    FOREIGN KEY (stayID) REFERENCES Stay(stayID),
    FOREIGN KEY (physicianID) REFERENCES Physician(physicianID),
    FOREIGN KEY (nurseID) REFERENCES Nurse(nurseID)
);

-- Create OnCall table
CREATE TABLE OnCall (
    nurseID INT PRIMARY KEY,
    startDate DATE,
    endDate DATE,
    FOREIGN KEY (nurseID) REFERENCES Nurse(nurseID)
);

-- Create Appointment table
CREATE TABLE Appointment (
    appID INT PRIMARY KEY,
    patientID INT,
    nurseID INT,
    physicianID INT,
    startDateTime DATETIME,
    endDateTime DATETIME,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID),
    FOREIGN KEY (nurseID) REFERENCES Nurse(nurseID),
    FOREIGN KEY (physicianID) REFERENCES Physician(physicianID)
);
