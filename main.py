from random import randint as randomnumber
import subprocess

words = ['Ocean', 'Waves', 'Apple', 'Glass', 'Grass', 'Delta', 'Bravo', 'Alpha']
symbols = ['!','£','$','%','^','&','*','@','?','#']


def runPSClip(cmd):
    completedBaseCommand = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completedBaseCommand

def createPSClip(password):
    command = "Write-Out '{}' | clip".format(password)
    return command


def generatePass(wordlist,symbollist):
    wordlistLen = len(wordlist) - 1
    symbollistLen = len(symbollist) - 1


    randomWord = wordlist[randomnumber(0,int(wordlistLen))]
    randomSymbol = symbollist[randomnumber(0,int(symbollistLen))]

    completedPass = randomWord + str(randomnumber(1,100)) + randomSymbol
    return completedPass


print(generatePass(words,symbols))

psClipCommand = createPSClip(generatePass(words,symbols))

runPSClip(psClipCommand)


