import os
import shutil
print("Please type the folder you wish to start in")
path = input()
startFolder = os.listdir(path)
#print("\n".join(startFolder))

print("please enter name of the folder you wish to move the files into")
moveFolder = str(input())

print("please type the keyword of the file names you want to move NOTE! Must be 5 letters only.")

nameOfFile = str(input())

zulu = 0

fileFound = []
y = 0
n = 0
for i in range(0, len(startFolder)):
    zulu = startFolder[n][0:5]
    if zulu == nameOfFile:
	    fileFound.insert(1,startFolder[n])
    n = n +1
#print(fileFound)
for i in range(0, len(fileFound)):
    move = fileFound[y]
    shutil.move(os.path.join(path, move), os.path.join(moveFolder))
    y = y + 1
    
print("you have moved the files")

goodbye = input()
