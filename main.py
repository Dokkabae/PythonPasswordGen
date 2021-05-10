from random import randint as randomnumber
import subprocess
from time import sleep

words = ['Ocean', 'Waves', 'Apple', 'Glass', 'Grass', 'Delta', 'Bravo', 'Alpha']
symbols = ['!','£','$','%','^','&','*','@','?','#']


def runPSClip(cmd):
    completedBaseCommand = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completedBaseCommand

def createPSClip(password):
    print(password)
    writeOutCommand = "Write-Output \'{}\' ".format(password)
    fullCommand = writeOutCommand + "| clip"
    return fullCommand


def generatePass(wordlist,symbollist):
    wordlistLen = len(wordlist) - 1
    symbollistLen = len(symbollist) - 1


    randomWord = wordlist[randomnumber(0,int(wordlistLen))]
    randomSymbol = symbollist[randomnumber(0,int(symbollistLen))]

    completedPass = randomWord + str(randomnumber(1,100)) + randomSymbol
    return completedPass

psClipCommand = createPSClip(generatePass(words,symbols))

runPSClip(psClipCommand)

input("Press any key to close")