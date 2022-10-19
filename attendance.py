#!/usr/bin/python3
import pandas as pd
import sys
import os
import csv

#find all csv files in a directory
def listFiles(path):
	paths = []
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.lower().endswith('.csv'):
				paths.append(os.path.join(root,file))
	return paths 

def createNamesAndSums(listOfCsvFiles):
	namesDict = {} # dictinary to save the names and the sum of duration from all files 
	for csvFile in listOfCsvFiles: #run on every csv file
		df = pd.read_csv(csvFile)
		#print(str(df["Meeting Start Time"]).rsplit(" "))
		count =0
		newIntDuration = [] #int value in every duration time.
        	#for loop to get the int value from the duration time
		for time in df["Attendance Duration"]:
			intTime = time.replace("mins","")
			newIntDuration.append(int(intTime))

	        #for loop to add the dictinary all the names with the sum of the duration time
		for name in df["Name"]:
			if name not in namesDict:
				namesDict[name] = newIntDuration[count]
			else:
				namesDict[name] += newIntDuration[count]
			count+=1
	return namesDict

def CreateCsv(namesDict):
	headers = ["Student Name", "Sum Of Duration Time"]
	#put the dict with all names and sums into csf file.
	with open('NewAttendance.csv','w') as csvfile:
		dw = csv.DictWriter(csvfile,delimiter = ",",fieldnames=headers)
		dw.writeheader()
		for key in namesDict.keys():
			csvfile.write('%s,%s\n' % (key,namesDict[key]))

def main():
#	if len(sys.argv) != 2:
#		return "please enter 1 argument"
#	else:
	path = "/home/noa/Downloads" #sys.argv[1]
	if os.path.isdir(path):
		listFiles(path)
		listOfCsvFiles = listFiles(path)
#		print("the csv files in this directory are:",listOfCsvFiles)
		namesDict = createNamesAndSums(listOfCsvFiles)
		CreateCsv(namesDict)
#		print(namesDict)
		return namesDict
		

#	else:
#		return "please enter a directory"


if __name__ == '__main__':
	main()




