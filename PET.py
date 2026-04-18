import os, time
#from tkinter import *

class Evidence:
    def __init__ (self, box=0, dots=0, emf=0, freezing=0, orb=0, uv=0, writing=0):
        self.box = box
        self.dots = dots
        self.emf = emf
        self.freezing = freezing
        self.orb = orb
        self.uv = uv
        self.writing = writing
        

    #def NazevMetody(self,)

ghostDict = {
    "Banshee": Evidence(dots=1, orb=1, uv=1),
    "Demon (Démon)": Evidence(freezing=1, uv=1, writing=1),
    "Dayan": Evidence(box=1, emf=1, orb=1),

    "Deogen": Evidence(box=1, dots=1, writing=1),
    "Gallu": Evidence(box=1, emf=1, uv=1),
    "Goryo": Evidence(dots=1, emf=1, uv=1),

    "Hantu": Evidence(freezing=1, orb=1, uv=1),
    "Jinn": Evidence(emf=1, freezing=1, uv=1),
    "Mare": Evidence(box=1, orb=1, writing=1),

    "Moroi": Evidence(box=1, freezing=1, writing=1),
    "Myling": Evidence(emf=1, uv=1, writing=1),
    "Obake": Evidence(emf=1, orb=1, uv=1),

    "Obambo": Evidence(dots=1, uv=1, writing=1),
    "Oni": Evidence(dots=1, emf=1, freezing=1),
    "Onryo": Evidence(box=1, freezing=1, orb=1),

    "Phantom (Fantom)": Evidence(box=1, dots=1, uv=1),
    "Poltergeist": Evidence(box=1, uv=1, writing=1),
    "Raiju": Evidence(dots=1, emf=1, orb=1),

    "Revenant": Evidence(freezing=1, orb=1, writing=1),
    "Shade": Evidence(emf=1, freezing=1, writing=1),
    "Spirit": Evidence(box=1, emf=1, writing=1),

    "Thaye": Evidence(dots=1, orb=1, writing=1),
    "The Mimic (Mimik)": Evidence(box=1, freezing=1, orb=1, uv=1),
    "The Twins (Dvojčata)": Evidence(box=1, emf=1, freezing=1),

    "Wraith": Evidence(box=1, dots=1, emf=1),
    "Yokai": Evidence(box=1, dots=1, orb=1),
    "Yurei": Evidence(dots=1, freezing=1, orb=1),    
}

evidenceDict = {
    "Spirit Box": 'spirit box',
    "D.O.T.S": 'dots',
    "EMF 5": 'emf',
    "Freezing": 'freezing',
    "Ghost Orbs": 'orb',
    "Ultraviolet": 'uv',
    "Ghost Writing": 'writing'
}

evidenceKeyDict = {
    "b": 'box',
    "d": 'dots',
    "e": 'emf',
    "f": 'freezing',
    "o": 'orb',
    "u": 'uv',
    "w": 'writing'
}

version = "v2.0.0"

try:
    os.remove("GhostEvidenceFile.txt")
    os.remove("InputEvidenceFile.txt")
except:
    pass

open("GhostEvidenceFile.txt", "x")
open("InputEvidenceFile.txt", "x")

def Clear(): #works - clears the console
    os.system('cls' if os.name == 'nt' else 'clear')

def ClearInputEvidenceFile(): #works - clears input evidence file
    os.remove("InputEvidenceFile.txt")
    open("InputEvidenceFile.txt", "x")

def EvidenceCheck(checkEvidence: str): #works - checks if the selected evidence hasnt already been used
    with open("InputEvidenceFile.txt", "r") as f:
        for line in f:
            if line.strip().strip("'") == checkEvidence:
                print("Evidence has already been registered!")
                return 1
    return 0

def WriteInputEvidenceFile(inputtedEvidence: str): #works - writes down the selected evidence in the file
    if EvidenceCheck(inputtedEvidence) != 1: 
        with open("InputEvidenceFile.txt", "a") as f:
            f.write(f"'{inputtedEvidence}'\n")

def ReadInputEvidenceFile(): #works - counts all lines and by that determines inputted evidence count
    with open("InputEvidenceFile.txt", "r") as f:
        inputtedEvidenceCount = 0
        for line in f:
            inputtedEvidenceCount = inputtedEvidenceCount + 1
        return inputtedEvidenceCount

def InitGhostEvidenceFile(): #works - creates the ghost evidence file with each ghost and their evidence
    with open("GhostEvidenceFile.txt", "a") as f:
        while True:
            for ghost, ghostAttributesttributes in ghostDict.items(): #name, evidence in dict with ghosts
                attributeTempDict = vars(ghostAttributesttributes)
                ghostNameWrite = f"{ghost};"
                f.write(ghostNameWrite) #writes ghost name first
                for attributeName, attributeValue in attributeTempDict.items(): #goes through all attributes in the temporary dictionary for each ghost
                    if(attributeValue == 1): #checks attribute value
                        attributeWriteString = f"'{attributeName}';" #makes evidence as 'evidence'
                        f.write(attributeWriteString) #writes that evidence down
                f.write("\n")
            break

def GhostEvidence(): #works - prints selected ghost's evidence
    Clear()
    desiredGhost = input("Which ghosts evidence do you want to check?\n> ").capitalize()
    with open("GhostEvidenceFile.txt", "r") as f:
        for line in f:
            lineArray = line.strip().split(';')
            if(lineArray[0] == desiredGhost): #if the name matches
                print(f"{desiredGhost}:\n") #print ghost name
                evidenceIndex = 1
                for evidenceString, evidenceKey in evidenceDict.items():
                    if(lineArray[evidenceIndex] == evidenceKey):
                        print(f"- {evidenceString}")
                        evidenceIndex = evidenceIndex + 1
                        if(lineArray[4] != ""):
                            print(f"- {lineArray[4]}")
        print("Invalid ghost name!")

def PossibleGhosts(evidenceCount: int): #works
    if(evidenceCount != 0):
        evidenceArray = []
        with open("InputEvidenceFile.txt", "r") as f:
            for line in f:
                lineString = line.strip().strip("")
                evidenceArray.append(lineString)
        with open("GhostEvidenceFile.txt", "r") as f:
            print("Possible ghosts:\n")
            for line in f: 
                lineArray = line.strip().split(';') 
                ghostName = lineArray[0] 
                matchingEvidence = 0
                for currentEvidence in evidenceArray:
                    if currentEvidence in lineArray:
                        matchingEvidence = matchingEvidence + 1
                if(matchingEvidence == evidenceCount): 
                    print(f"- {ghostName}")
    else:
        print("All the ghosts!")

def IdentifyGhost():
    identificationGhost = []
    with open("InputEvidenceFile.txt", "r") as f:
        for line in f:
            formattedLine = line.strip()
            identificationGhost.append(formattedLine)
    if(len(identificationGhost) == 0):
        return ""
    if(len(identificationGhost) > 4):
        print("Can't be any ghost!")
        return ""
    possibleCount = 0
    foundGhost = ""
    with open("GhostEvidenceFile.txt", "r") as f:
        for line in f:
            lineArray = line.strip().split(';')
            ghostName = lineArray[0]
            matchingEvidence = 0
            for currentEvidence in identificationGhost:
                if currentEvidence in lineArray:
                    matchingEvidence = matchingEvidence + 1
            if(matchingEvidence == len(identificationGhost)):
                possibleCount = possibleCount + 1
                foundGhost = ghostName
    if(possibleCount == 1):
        print(f"\nGhost identified: {foundGhost}!")
        return foundGhost
    elif(possibleCount == 0):
        print("Can't be any ghost!")
        return ""
    return ""

def DeleteSpecificEvidence(a: str): #works - deletes specified evidence
    if len(a) < 3:
        print("Invalid input format! Use '2 <space> <key>'")
        return
    evidenceKey = a[2]
    evidenceToRemove = ""
    for dictKey, dictValue in evidenceKeyDict.items(): 
        if dictKey == evidenceKey:
            evidenceToRemove = dictValue
            break
    if evidenceToRemove == "":
        print("Unknown evidence key!")
        return
    evidenceArray = []
    with open("InputEvidenceFile.txt", "r") as f:
        for line in f:
            cleanLine = line.strip().strip("'")
            evidenceArray.append(cleanLine)
    if evidenceToRemove in evidenceArray:
        evidenceArray.remove(evidenceToRemove)
    else:
        print("This evidence hasn't been registered yet!")
        return
    with open("InputEvidenceFile.txt", "w") as f:
        for remainingEvidence in evidenceArray:
            f.write(f"'{remainingEvidence}'\n")
    print(f"Evidence '{evidenceToRemove}' has been removed.")

def Main():

    InitGhostEvidenceFile()

    evidenceCount = 0
    evidenceArray = ["Spirit Box", "D.O.T.S", "EMF 5", "Freezing", "Ghost Orbs", "Ultraviolet", "Ghost Writing"]
    evidenceIndexArray = [0,0,0,0,0,0,0]
    identificationGhost = Evidence()

    while True:

        evidenceCount = ReadInputEvidenceFile()
        if(evidenceCount >= 1):
            print(f"Select a piece of evidence ( {evidenceCount} / 4 ):")
        else:
            print("Select a piece of evidence:")
        print("-----")

        print("[B] - Spirit Box")
        print("[D] - D.O.T.S")
        print("[E] - EMF 5")
        print("[F] - Freezing")
        print("[O] - Ghost Orbs")
        print("[U] - Ultraviolet")
        print("[W] - Ghost Writing")
        
        print("\n[1] - Exit")
        print("[2] - Clear Specific Evidence (2 <space> evidence key)")
        print("[3] - Clear All Evidence")
        print("[4] - Possible Ghosts")
        print("[5] - Ghost Evidence")
        print("-----")

        choice = input("> ").lower()
        try:
            choice = int(choice)
        except:
            pass

        if(type(choice) == str):
            if(choice == "b"):
                WriteInputEvidenceFile("box")
            elif(choice == "d"):
               WriteInputEvidenceFile("dots")
            elif(choice == "e"):
                WriteInputEvidenceFile("emf")
            elif(choice == "f"):
                WriteInputEvidenceFile("freezing")
            elif(choice == "o"):
                WriteInputEvidenceFile("orb")
            elif(choice == "u"):
               WriteInputEvidenceFile("uv")
            elif(choice == "w"):
                WriteInputEvidenceFile("writing")
            else:
                if(choice[0] == "2"): #choice - 2
                    DeleteSpecificEvidence(choice)
                else:
                    print("Incorrect input!!")
        else:
            if(choice == 1):
                break
            elif(choice == 3):
                ClearInputEvidenceFile()
            elif(choice == 4):
                PossibleGhosts(evidenceCount)
            elif(choice == 5):
                GhostEvidence()
            else:
                print("Incorrect input!")

        found = IdentifyGhost()
        if(found != ""):
            exitChoice = input("\nDo you want to exit? (y/n)\n> ").lower()
            if(exitChoice == "y"):
                ClearInputEvidenceFile()
                return 1
            else:
                ClearInputEvidenceFile()
                return 0

    ClearInputEvidenceFile()
    return 1

while True:
    trueEnd = Main()
    try:
        os.remove("GhostEvidenceFile.txt")
        os.remove("InputEvidenceFile.txt")
    except:
        pass

    open("GhostEvidenceFile.txt", "x")
    open("InputEvidenceFile.txt", "x")
    
    if(trueEnd == 1):
        break