from random import randint as randomnumber
import subprocess

words = ['Ocean', 'Waves', 'Apple', 'Glass', 'Grass', 'Delta', 'Bravo', 'Alpha']
symbols = ['!','£','$','%','^','&','*','@','?','#']

def runPS(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def generatePass(wordlist,symbollist):
    completedPass = (str(wordlist[randomnumber(0,(int(len(words)) - 1))]) + str(randomnumber[1,100]) + str(symbollist[randomnumber(0,(int(len(symbols)) - 1))]))
    return completedPass


print(generatePass(words,symbols))

#runPS("Write-Out '{}' \| clip").format(geberatePass())

