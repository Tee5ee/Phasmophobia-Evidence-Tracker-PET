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

version = "v2.0.0"

try:
    os.remove("GhostEvidenceFile.txt")
    os.remove("InputEvidenceFile.txt")
except:
    pass

open("GhostEvidenceFile.txt", "x")
open("InputEvidenceFile.txt", "x")

def Clear(): #works
    os.system('cls' if os.name == 'nt' else 'clear')

def ClearInputEvidenceFile(): #works
    os.remove("InputEvidenceFile.txt")
    open("InputEvidenceFile.txt", "x")

def EvidenceCheck(checkEvidence: str): #works
    with open("InputEvidenceFile.txt", "r") as f: #if its been used - 1 if not - 0 NOT WORKING CHECK LOGIC
        for line in f:
            print(checkEvidence)
            if(line == checkEvidence):   
                print("Evidence has already been registered!")
                return 1
    return 0

def WriteInputEvidenceFile(inputtedEvidence: str): #DONT WRITE EVIDENCE WHEN ITS ALREADY BEEN REGISTERED NOT WORKING
    funcContinue = EvidenceCheck(inputtedEvidence)
    if(funcContinue != 1):   
        with open("InputEvidenceFile.txt", "a") as f:
            f.write(f"'{inputtedEvidence}'\n")
    print(funcContinue)

def ReadInputEvidenceFile(): #works
    with open("InputEvidenceFile.txt", "r") as f:
        inputtedEvidenceCount = 0
        for line in f:
            inputtedEvidenceCount = inputtedEvidenceCount + 1
        return inputtedEvidenceCount

def InitGhostEvidenceFile(): #works
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

def GhostEvidence(): #works
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

def PossibleGhosts(evidenceCount: int): #not finished
    if(evidenceCount != 0):
        evidenceArray = []
        with open("InputEvidenceFile.txt", "r") as f:
            for line in f:
                lineString = line.strip().strip("")
                evidenceArray.append(lineString)
        with open("GhostEvidenceFile.txt", "r") as f:
            print("Possible ghosts:\n")
            for line in f: #for each line in all lines
                lineArray = line.strip().split(';') #strips "" and splits using ;
                lineArrayIndex = 1
                matchingEvidence = 0
                for lineElements in range(len(lineArray)):
                    ghostName = lineArray[0]
                    for iteration in range(len(evidenceArray)):
                        if(lineArray[lineArrayIndex] == evidenceArray[iteration]):
                            matchingEvidence = matchingEvidence + 1
                            if(matchingEvidence == evidenceCount): #if the number of matching evidence equals to the evidence count
                                print(f"- {ghostName}")
                            break
                        lineArrayIndex = lineArrayIndex + 1
    else:
        print("All the ghosts!")

def IdentifyGhost(): #not finished
    identificationGhost = []
    with open("InputEvidenceFile.txt", "r") as f: #load evidence into the array
        for line in f:
            formattedLine = line.strip().strip("'")
            identificationGhost.append(formattedLine)
    if(len(identificationGhost) > 4):
        print("Can't be any ghost!")
    print(identificationGhost)

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
        print("[2] - Clear Evidence")
        print("[3] - Possible Ghosts")
        print("[4] - Ghost Evidence")
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
                print("Incorrect input!")
        else:
            if(choice == 1):
                break
            elif(choice == 2):
                ClearInputEvidenceFile()
            elif(choice == 3):
                PossibleGhosts(evidenceCount)
            elif(choice == 4):
                GhostEvidence()
            else:
                print("Incorrect input!")

        IdentifyGhost()

    ClearInputEvidenceFile()
    return 1

while True:
    trueEnd = Main()
    if(trueEnd == 1):
        break