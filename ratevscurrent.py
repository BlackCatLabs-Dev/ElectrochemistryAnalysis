#!/bin/usr/python

import numpy as np
import os
import sys


#check for number of arguments
if sys.argv[1] ==('-h' or '-help') or len(sys.argv)!=3:
	print('[1]=working directory')
	print('[2]=path to output file')
	print('')
	print('All arguments required')
	sys.exit()
#Var intialization
wd=sys.argv[1]
#print('working directory: '+wd)

Flist=os.listdir(wd)
#print(Flist)

#create list for output
output=[]

for F in Flist:
	#print(F)
	data=open(wd+F).readlines()
	#print(data)
	Flag=0
	Odata=[]

	for line in data:
		#print(line)
		if line.startswith("SCANRATE"):
			Rate=line.strip().split()
			#print(Rate)
		if Flag==0:
			Temp=line.strip().split()
			if len(Temp)!=0:
				if Temp[0]=='#':
					Flag=1
					continue
				else:
					pass
		if Flag==1:
			Temp=line.strip().split()
			#print(Temp)
			Odata.append(float(Temp[3]))
	#print(Odata)
	
	#get output file name from input file name
	#oname=F[:-4]
        #print(oname)

        #cast output data array as a numpy array
	Odata=np.asarray(Odata)
	#print(Odata)

	start = 99
	end = 101
	#Get range of data to analyize
	sample_range=Odata[start:end+1]

	avg=np.average(sample_range)
	#print(Rate[2],avg)
	output.append([float(Rate[2]),avg])

#print(output)
output=sorted(output)	

#for o in output:
#	print(o)
outdata=np.asarray(output)
print(outdata)
print(type(outdata))
np.savetxt(sys.argv[2],outdata)
