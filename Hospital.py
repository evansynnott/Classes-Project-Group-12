'''
classesproject.py

Written by Tyler Hynes, Coltan Rozander, and Evan Synnott-Hilliard

This Program does things

'''
import re


class Doctor: 
    def __init__(self, id, name, specialization, working_time, qualification, room_number) -> None:
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f'{self.name} with employee id{self.id} is a doctor.'

    def formatDrInfo(propertiesValuesList): #Formats each doctor’s information (properties) in the same format used in the .txt file (i.e., has underscores between values)
        spaces = [5, 23, 16, 16, 16, 12]
        formattedText = ""

        for item in propertiesValuesList:
            formattedText += item + \
                (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterDrInfo(self): #Asks the user to enter doctor properties (listed in the Properties point)
        self.id = input("Enter the Doctor's ID: \n")
        self.name = input("Enter the Doctor's name: \n")
        self.specialization = input("Enter the Doctor's specialty: \n")
        self.workingTime = input(
            "Enter the Doctor's timing (e.g., 7am-10pm): \n")
        self.qualification = input("Enter the Doctor's qualification: \n")
        self.roomNumber = input("Enter the Doctor's room number: \n")

        self.addDrToFile(self)

    def readDoctorsFile(): #Reads from “doctors.txt” file and fills the doctor objects in a list
        path = "data\doctors.txt"
        doctorsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    doctor = Doctor(line[0], line[1], line[2],
                                    line[3], line[4], line[5])

                    doctorsObjectList.append(doctor)

            file.close()
        except IOError:
            file = open(path, 'a+')
            print("doctors.txt file created")

        return doctorsObjectList

    def searchDoctorById(idSearch): #Searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
        doctorsObjectList = Doctor.readDoctorsFile()
        idExist = False
        for doctor in doctorsObjectList:
            if doctor.id == idSearch:
                doctor.displayDoctorInfo()
                idExist = True
                return doctorsObjectList.index(doctor)
        if idExist == False:
            print("Can't find the doctor with the same ID on the system \n")
            return -1

    def searchDoctorByName(nameSearch): #Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
        doctorsObjectList = Doctor.readDoctorsFile()
        nameExist = False

        for doctor in doctorsObjectList:
            if doctor.name == nameSearch:
                doctor.displayDoctorInfo()
                nameExist = True
        if nameExist == False:
            print("Can't find the doctor with the same name on the system \n")
            return -1

    def displayDoctorInfo(self): #Displays doctor information on different lines, as a list
        headerList = ["ID", "Name", "Specialty",
                      "Timing", "Qualification", "Room Number"]
        print(Doctor.formatDrInfo(headerList) + "\n")
        valuesList = [self.id, self.name, self.specialization,
                      self.workingTime, self.qualification, self.roomNumber]
        print(Doctor.formatDrInfo(valuesList))

    def readDoctorsFile(): #Asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
        path = "data\doctors.txt"
        doctorsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    doctor = Doctor(line[0], line[1], line[2], line[3], line[4], line[5])

                    doctorsObjectList.append(doctor)

            file.close()
        except IOError:
            file = open(path, 'a+')
            print("doctors.txt file created")

        return doctorsObjectList

    def displayDoctorsList(): #Displays all the doctors’ information, read from the file, as a report/table
        path = "data\doctors.txt"
        headerList = ["ID", "Name", "Specialty",
                      "Timing", "Qualification", "Room Number"]
        headerSpaces = [5, 23, 16, 16, 16, 12]
        for item in headerList:
            print(
                item + (" " * (headerSpaces[headerList.index(item)] - len(item))), end="")
        print("\n")
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def writeListOfDoctorsToFile(doctorsObjectList): #Writes the list of doctors to the doctors.txt file after formatting it correctly
        path = "data\doctors.txt"
        file = open(path, "r+")
        textOutput = ""
        for dr in doctorsObjectList:
            drProperties = [dr.id, dr.name, dr.specialization,
                            dr.workingTime, dr.qualification, dr.roomNumber]
            ft = Doctor.formatDrInfo(drProperties)
            textOutput += ft + "\n\n"

        file.truncate(0)
        file.write(textOutput)
        file.close()

    def addDrToFile(drObject): #Writes doctors to the doctors.txt file after formatting it correctly
        path = "data\doctors.txt"
        textOutput = ""

        file = open(path, "a")
        dr = drObject
        drProperties = [dr.id, dr.name, dr.specialization,
                        dr.workingTime, dr.qualification, dr.roomNumber]

        addText = Doctor.formatDrInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()


class Facility:
    information = 'facility information'

    def __init__(self, facility_name) -> None:
        self.facility_name = facility_name

    def __str__(self):
        return f'{self.facility_name} is a facility location.'

    def addFacility(self): #Displays the list of facilities
        fname = input("Enter Facility name: \n")
        self.name = fname
        path = "data\facilities.txt"
        with open(path, "a") as file:
            file.write(self.name + "\n\n")

    def displayFacilities(): #Displays the list of facilities
        print("The Hospital  Facilities are: \n\n")
        path = "data\facilities.txt"
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    def writeListOfFacilitiesToFile(facilityList): #Writes the facilities list to facilities.txt
        path = "data\faclities.txt"
        with open(path, "r+") as file:
            for facility in facilityList:
                file.write(facility + "\n\n")


class Laboratory:
    information = 'laboratory information'

    def __init__(self, lab_name, cost) -> None:
        self.lab_name = lab_name
        self.cost = cost

    def __str__(self):
        return f'{self.lab_name} is a lab location.'

    def addLabToFile(labObject): #Adds and writes the lab name to the file in the format of the data that is in the file
        path = "data\laboratories.txt"
        textOutput = ""

        file = open(path, "a")
        labPropertiesList = [labObject.name, labObject.cost]

        addText = Laboratory.formatLabInfo(labPropertiesList)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

    def writeListOfLabsToFile(labObjectsList): #Writes the list of labs into the file laboratories.txt
        path = "data\laboratories.txt"
        file = open(path, "r+")
        textOutput = ""
        for lab in labObjectsList:
            labPropertiesList = [lab.name, lab.cost]
            ft = Laboratory.formatLabInfo(labPropertiesList)
            textOutput += ft + "\n\n"

        file.truncate(0)
        file.write(textOutput)
        file.close()

    def displayLabList(): #Writes the list of labs into the file laboratories.txt
        path = "data\laboratories.txt"
        headerList = ["Lab", "Cost"]
        print(Laboratory.formatLabInfo(headerList))
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def formatLabInfo(propertiesValuesList): #Formats the Laboratory object similar to the laboratories.txt file
        spaces = [16, 16]
        formattedText = ""

        for item in propertiesValuesList:
            formattedText += item + \
                (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterLaboratoryInfo(self): #Asks the user to enter lab name and cost and forms a Laboratory object
        self.name = input("Enter Laboratory facility: \n")
        self.cost = input("Enter Laboratory cost: \n")

        Laboratory.addLabToFile(self)

    def readLaboratoriesFile(): #Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
        path = "data\laboratories.txt"
        labsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    lab = Laboratory(line[0], line[1])

                    labsObjectList.append(lab)

            file.close()
        except IOError:
            file = open(path, 'a+')
            print("laboratories.txt file created")

        return labsObjectList


class Patient:
    def __init__(self, pid, name, disease, gender, age) -> None:
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.name} is a {self.age} year old {self.gender} affected with {self.disease}'

    def formatPatientInfo(propertiesValuesList): #Formats patient information to be added to the file
        spaces = [5, 23, 16, 16, 16]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + \
                (" " * (spaces[propertiesValuesList.index(item)] - len(item))) #
        return formattedText

    def enterPatientInfo(self): #Asks the user to enter the patient info 
        self.id = input("Enter the Patients's ID: \n")
        self.name = input("Enter the Patients's name: \n")
        self.disease = input("Enter the Patient's Disease: \n")
        self.gender = input("Enter the Patient's Gender: \n")
        self.age = input("Enter the Patient's Age: \n")

    def readPatientsFile(): #Reads from file patients.txt
        path = "data\patients.txt"
        patientsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    patient = Patient(line[0], line[1],
                                      line[2], line[3], line[4])

                    patientsObjectList.append(patient)

            file.close()
        except IOError:
            file = open(path, 'a+')
            print("patients.txt file created")

        return patientsObjectList

    def searchPatientById(idSearch): #Searches for a patient using their ID
        patientsObjectList = Patient.readPatientsFile()
        idExist = False
        for patient in patientsObjectList:
            if patient.id == idSearch:
                patient.displayPatientInfo()
                idExist = True
                return patientsObjectList.index(patient)
        if idExist == False:
            print("Can't find the doctor with the same ID on the system \n")
            return -1

    def displayPatientInfo(self): #Displays patient info
        headerList = ["ID", "Name", "Disease", "Gender", "Age"]
        print(Patient.formatPatientInfo(headerList) + "\n")
        valuesList = [self.id, self.name, self.disease, self.gender, self.age]
        print(Patient.formatPatientInfo(valuesList))

    def editPatientInfo(): #Asks the user to edit patient information
        pt_Id = input(
            "Please enter the id of the doctor that you want to edit their information:\n")
        pt_index = Patient.searchPatientById(pt_Id)
        if pt_index != -1:
            ptObjList = Patient.readPatientsFile()
            ptObjList[pt_index].name = input("Enter new Name: \n")
            ptObjList[pt_index].disease = input("Enter new disease: \n")
            ptObjList[pt_index].gender = input("Enter new gender: \n")
            ptObjList[pt_index].age = input("Enter new age: \n")
            Patient.writeListOfPatientsToFile(ptObjList)
        else:
            return -1

    def displayPatientsList(): #Displays the list of patients
        path = "\data\patients.txt"
        headerList = ["ID", "Name", "Disease", "Gender", "Age"]
        headerSpaces = [5, 23, 16, 16, 16]
        for item in headerList:
            print(
                item + (" " * (headerSpaces[headerList.index(item)] - len(item))), end="")
        print("\n")
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def writeListOfPatientsToFile(patientsObjectList): #Writes a list of patients into the patients.txt file
        path = "data\patients.txt"
        file = open(path, "r+")
        textOutput = ""
        for pt in patientsObjectList:
            ptProperties = [pt.pid, pt.name, pt.disease, pt.gender, pt.age]
            ft = Patient.formatPatientInfo(ptProperties)
            textOutput += ft + "\n\n"

        file.truncate(0)
        file.write(textOutput)
        file.close()

    def addPatientToFile(ptObject): #Adds a new patient to the file
        path = "data\patients.txt"
        textOutput = ""

        file = open(path, "a")
        pt = ptObject
        drProperties = [pt.pid, pt.name, pt.disease, pt.gender, pt.age]

        addText = Patient.formatPatientInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()