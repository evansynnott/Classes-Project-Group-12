import Hospital as hs


def doctorMenu():
    runMenu = True
    print("Doctors Menu: \n1 - Display Doctors list \n2 - Search for doctor by ID\n3 - Search for doctor by name \n4 - Add doctor \n5 - Edit doctor info \n6 - Back to the Main Menu")
    userInput = input()
    if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3 and int(userInput) != 4 and int(userInput) != 5 and int(userInput) != 6:
        print("Wrong Input, Try again: ")
    elif int(userInput) == 1:
        print("displaying Doctors List")
        hs.displayDoctorsList
    elif int(userInput) == 2:
        docID = input("Enter the Doctor Id: ")
        hs.searchDoctorById(docID)
    elif int(userInput) == 3:
        docName = input("Enter the Doctor name: ")
        hs.searchDoctorByName(docName)
    elif int(userInput) == 4:
        hs.enterDrInfo()
    elif int(userInput) == 5:
        hs.editDoctorInfo
    elif int(userInput) == 6:
        runMenu = False
        return
'''
def Patients:

def Labatory:

def Facilities:
'''
runProgram = True
while runProgram == True:
    print("Welcome to Alberta Hospital (AH) Managment system \n Select from the following options, or select 0 to stop: \n1 - Doctors \n2 - Facilities\n3 - Laboratories \n4 - Patients")
    userInput = input()
    if userInput.isdigit() == False or int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3 and int(userInput) != 4 and int(userInput) != 0:
        print("Wrong Input, Try again")
    elif int(userInput) == 1:
        doctorMenu()
    elif int(userInput) == 2:
        print()
    elif int(userInput) == 3:
        print()
    elif int(userInput) == 4:
        print()
    elif int(userInput) == 0:
        runProgram = False
