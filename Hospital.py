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


def formatDrInfo(propertiesValuesList):
    spaces = [5, 23, 16, 16, 16, 12]
    formattedText = ""

    for item in propertiesValuesList:
        formattedText += item + \
            (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
    return formattedText


def enterDrInfo(self):
    self.id = input("Enter the Doctor's ID: \n")
    self.name = input("Enter the Doctor's name: \n")
    self.specialization = input("Enter the Doctor's specialty: \n")
    self.workingTime = input("Enter the Doctor's timing (e.g., 7am-10pm): \n")
    self.qualification = input("Enter the Doctor's qualification: \n")
    self.roomNumber = input("Enter the Doctor's room number: \n")

    self.addDrToFile(self)


def readDoctorsFile():
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


def searchDoctorById(idSearch):
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


def searchDoctorByName(nameSearch):
    doctorsObjectList = Doctor.readDoctorsFile()
    nameExist = False

    for doctor in doctorsObjectList:
        if doctor.name == nameSearch:
            doctor.displayDoctorInfo()
            nameExist = True
    if nameExist == False:
        print("Can't find the doctor with the same name on the system \n")
        return -1


def displayDoctorInfo(self):
    headerList = ["ID", "Name", "Specialty",
                  "Timing", "Qualification", "Room Number"]
    print(Doctor.formatDrInfo(headerList) + "\n")
    valuesList = [self.id, self.name, self.specialization,
                  self.workingTime, self.qualification, self.roomNumber]
    print(Doctor.formatDrInfo(valuesList))


def editDoctorInfo():
    dr_Id = input(
        "Please enter the id of the doctor that you want to edit their information:\n")
    dr_index = Doctor.searchDoctorById(dr_Id)
    if dr_index != -1:
        drObjList = Doctor.readDoctorsFile()
        drObjList[dr_index].name = input("Enter new Name: \n")
        drObjList[dr_index].specialization = input(
            "Enter new Specialist in: \n")
        drObjList[dr_index].workingTime = input("Enter new Timing: \n")
        drObjList[dr_index].qualification = input(
            "Enter new Qualification: \n")
        drObjList[dr_index].roomNumber = input("Enter new Room Number: \n")
        Doctor.writeListOfDoctorsToFile(drObjList)
    else:
        return -1


def displayDoctorsList():
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


def writeListOfDoctorsToFile(doctorsObjectList):
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


def addDrToFile(drObject):
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

    def addFacility(self):
        fname = input("Enter Facility name: \n")
        self.name = fname
        path = "data\facilities.txt"
        with open(path, "a") as file:
            file.write(self.name + "\n\n")

    def displayFacilities():
        print("The Hospital  Facilities are: \n\n")
        path = "data\facilities.txt"
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    def writeListOfFacilitiesToFile(facilityList):
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

    def addLabToFile(labObject):
        path = "data\laboratories.txt"
        textOutput = ""

        file = open(path, "a")
        labPropertiesList = [labObject.name, labObject.cost]

        addText = Laboratory.formatLabInfo(labPropertiesList)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

    def writeListOfLabsToFile(labObjectsList):
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

    def displayLabList():
        path = "data\laboratories.txt"
        headerList = ["Lab", "Cost"]
        print(Laboratory.formatLabInfo(headerList))
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def formatLabInfo(propertiesValuesList):
        spaces = [16, 16]
        formattedText = ""

        for item in propertiesValuesList:
            formattedText += item + \
                (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory facility: \n")
        self.cost = input("Enter Laboratory cost: \n")

        Laboratory.addLabToFile(self)

    def readLaboratoriesFile():
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

    def formatPatientInfo(propertiesValuesList):
        spaces = [5, 23, 16, 16, 16]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + \
                (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterPatientInfo(self):
        self.id = input("Enter the Patients's ID: \n")
        self.name = input("Enter the Patients's name: \n")
        self.disease = input("Enter the Patient's Disease: \n")
        self.gender = input("Enter the Patient's Gender: \n")
        self.age = input("Enter the Patient's Age: \n")

    def readPatientsFile():
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

    def searchPatientById(idSearch):
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

    def displayPatientInfo(self):
        headerList = ["ID", "Name", "Disease", "Gender", "Age"]
        print(Patient.formatPatientInfo(headerList) + "\n")
        valuesList = [self.id, self.name, self.disease, self.gender, self.age]
        print(Patient.formatPatientInfo(valuesList))

    def editPatientInfo():
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

    def displayPatientsList():
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

    def writeListOfPatientsToFile(patientsObjectList):
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

    def addPatientToFile(ptObject):
        path = "data\patients.txt"
        textOutput = ""

        file = open(path, "a")
        pt = ptObject
        drProperties = [pt.pid, pt.name, pt.disease, pt.gender, pt.age]

        addText = Patient.formatPatientInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()