#!/bin/usr/python
  
import numpy as np
import os
import sys

#check for number of arguments
if sys.argv[1] ==('-h' or '-help') or len(sys.argv)!=2:
	print('[1]=working directory')
	print('')
	print('All arguments required')
	sys.exit()

#Var intialization
wd=sys.argv[1]
print('working directory: '+wd)
Flist=os.listdir(wd)
print(Flist)
wd=sys.argv[1]
print('working directory: '+wd)
Flist=os.listdir(wd)
print(Flist)

for F in Flist:
	print(F)
	data=open(wd+F).readlines()
	#print(data)
	Flag=0
	Odata=[]

	for line in data:
                #print(line)
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
			Odata.append((float(Temp[1]),float(Temp[2])))

        #get output file name from input file name
	Oname = F[:-4]
        #print(oname)

        #cast output data array as a numpy array
	Odata=np.asarray(Odata)
        #print(Odata)

        

        #save output
	np.savetxt(wd+Oname+'_xy.txt',Odata, header='#'+Oname+'_T, #'+Oname+'_V')
