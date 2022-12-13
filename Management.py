'''
classesproject.py

Written by Tyler Hynes, Coltan Rozander, and Evan Synnott-Hilliard

This Program does things

'''
from Hospital import Doctor as Doc
from Hospital import Laboratory as Lab
from Hospital import Facility as Fac
from Hospital import Patient as Pat


def doctorMenu():
    runMenu = True
    while runMenu == True:
        print("\nDoctors Menu: \n1 - Display Doctors list \n2 - Search for doctor by ID\n3 - Search for doctor by name \n4 - Add doctor \n5 - Edit doctor info \n6 - Back to the Main Menu")
        userInput = input()
        if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3 and int(userInput) != 4 and int(userInput) != 5 and int(userInput) != 6:
            print("Wrong Input, Try again: ")
        elif int(userInput) == 1:
            Doc.displayDoctorsList()
        elif int(userInput) == 2:
            docID = input("Enter the Doctor Id: ")
            Doc.searchDoctorById(docID)
        elif int(userInput) == 3:
            docName = input("Enter the Doctor name: ")
            Doc.searchDoctorByName(docName)
        elif int(userInput) == 4:
            Doc.enterDrInfo()
        elif int(userInput) == 5:
            docID = input("Enter the Doctor Id: ")
            Doc.editDoctorInfo(docID)
        elif int(userInput) == 6:
            runMenu = False
            return

def FacMenu():
    runMenu = True
    while runMenu == True:
        print("\nFacilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu")
        userInput = input()
        if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3:
            print("Wrong Input, Try again: ")
        elif int(userInput) == 1:
            Fac.displayFacilities()
        elif int(userInput) == 2:
            newLab = input("Insert Name of laboratory")
            Fac.addFacility()
        elif int(userInput) == 3:
            runMenu = False
            return  

def labMenu():
    runMenu = True
    while runMenu == True:
        print("\nLaboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu")
        userInput = input()
        if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3:
            print("Wrong Input, Try again: ")
        elif int(userInput) == 1:
            Lab.displayLabList()
        elif int(userInput) == 2:
            newLab = input("Insert Name of laboratory")
            Lab.addLabToFile()
        elif int(userInput) == 3:
            runMenu = False
            return

def PatMenu():
    runMenu = True
    while runMenu == True:
        print("\nPatients Menu: \n1 - Display patients list \n2 - Search for patient by ID\n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu")
        userInput = input()
        if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3 and int(userInput) != 4 and int(userInput) != 5:
            print("Wrong Input, Try again: ")
        elif int(userInput) == 1:
            Pat.displayPatientsList()
        elif int(userInput) == 2:
            patID = input("Enter the Patient Id: ")
            Pat.searchPatientById(patID)
        elif int(userInput) == 3:
            Pat.enterPatientInfo
        elif int(userInput) == 4:
            docID = input("Enter the Doctor Id: ")
            Pat.editPatientInfo(patID)
        elif int(userInput) == 5:
            runMenu = False
            return

runProgram = True
while runProgram == True:
    print("\nWelcome to Alberta Hospital (AH) Managment system \nSelect from the following options, or select 0 to stop: \n1 - Doctors \n2 - Facilities\n3 - Laboratories \n4 - Patients")
    userInput = input()
    if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3 and int(userInput) != 4 and int(userInput) != 0:
        print("Wrong Input, Try again")
    elif int(userInput) == 1:
        doctorMenu()
    elif int(userInput) == 2:
        FacMenu()
    elif int(userInput) == 3:
        labMenu()
    elif int(userInput) == 4:
        PatMenu()
    elif int(userInput) == 0:
        runProgram = False
