"""
CPRG216-D
Assignment 4

Colton Rozander
908292


"""

class Doctor:
    def __init__(self,docID,docName,docSpec,workingTime,qualification,roomNumber) -> None:
        self.docID = docID
        self.docName = docName
        self.docSpec = docSpec
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber

    def formatDrInfo(self,docID,docName,docSpec,workingTime,qualification,roomNumber):
        formatDr = (f"\n{docID}_{docName}_{docSpec}_{workingTime}_{qualification}_{roomNumber}")
        return formatDr
    
    def addDrToFile():
        file = open("doctors.txt", "a")
        file.write(formatDrInfo())
        file.close()

    def readDoctorsFile():
        doctorList = open("doctors.txt", "r")
        for line in doctorList:
            docLine = line.split("_")
            docID = docLine[0]
            docName = docLine[1]
            docSpec = docLine[2]
            workingTime = docLine[3]
            qualification = docLine[4]
            roomNumber = docLine[5]
            Doctor(docID,docName,docSpec,workingTime,qualification,roomNumber)
        doctorList.close()

    def enterDrInfo():
        docID = input("Enter the Doctor's ID: \n")
        docName = input("Enter the Doctor's Name: \n")
        docSpec = input("Enter the Doctor's Specialization: \n")
        workingTime = input("Enter the Doctor's Timing (e.g., 7am-10pm): \n")
        qualification = input("Enter the Doctor's Qualifications: \n")
        roomNumber = input("Enter the Doctor's Room Number: \n")
        return Doctor(docID,docName,docSpec,workingTime,qualification,roomNumber)

    def searchDocByID():
        doctorsObjectList = Doctor.readDoctorsFile()
        return

    def searchDocByName():
        return

    def displayDocInfo():
        return

    def editDocInfo():
        return

    def displayDocList():
        return


class Facility:
    def __init__(self,facilityName) -> None:
        self.facilityName = facilityName

    def addFacility():
        return

    def displayFacilities():
        return

    def writeListOfFacilitiesToFile():
        return


class Laboratory:
    def __init__(self,labName,labCost) -> None:
        self.labName = labName
        self.labCost = labCost

    def addLabToFile():
        return

    def writeListOfLabsToFile():
        return

    def displayLabsList():
        return

    def formatDrInfo():
        return

    def enterLaboratoryInfo():
        return

    def readLaboratoriesFile():
        return


class Patient:
    def __init__(self,patID,patName,patDisease,patGender,patAge) -> None:
        self.patID = patID
        self.patName = patName
        self.patDisease = patDisease
        self.patGender = patGender
        self.patAge = patAge

    def formatPatInfo():
        return

    def enterPatInfo(self):
        self.patID = input("Enter the Patient's ID: \n")
        self.patName = input("Enter the Patient's Name: \n")
        self.patDisease = input("Enter the Patient's Disease: \n")
        self.patGender = input("Enter the Patient's Gender: \n")
        self.patAge = input("Enter the Patient's Age: \n")

    def readPatFile():
        return

    def searchPatByID():
        return

    def displayPatInfo():
        return

    def editPatInfo():
        return

    def displayPatList():
        return

    def writeListOfPatsToFile():
        return

    def addPatToFile():
        return