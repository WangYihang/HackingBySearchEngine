import os
import sys
import platform
# config-start
resultFilePath = "./WaitingForFiltration/"
resultFileName = "Results.txt"
# config-end
if platform.system() == "Windows":
	separator = "\\"
else:
	separator = "/"
root = "." + separator + "Results" + separator
scriptpath = sys.argv[0]
scriptfilename = scriptpath.split(separator)[-1]
files = []
for i in os.listdir(root):
	if os.path.isfile(os.path.join(root,i)):
		files.append(i)

print files

if resultFileName in files:
	files.remove(resultFileName)
if scriptfilename in files:
	files.remove(scriptfilename)

print files
resultFile = open(resultFilePath + resultFileName,"w")
for file in files:
	tempFile = open(root + file,"r")
	for line in tempFile:
		resultFile.write(line)
resultFile.close()