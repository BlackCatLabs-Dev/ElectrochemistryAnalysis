#!/bin/usr/python

import numpy as np
import os
import sys

#check for number of arguments 
if sys.argv[1] ==('-h' or '-help') or len(sys.argv)!=5:
	print('[1]=working directory') 
	print('[2]=Volt_offset') 
	print('[3]=current_scale') 
	print('[4]=electrode_area') 
	print('')
	print('All arguments required')
	sys.exit()

#Var intialization
wd=sys.argv[1] 
print('working directory: '+wd)
Volt_offset=float(sys.argv[2])
current_scale=float(sys.argv[3])
electrode_area=float(sys.argv[4])
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
			Odata.append([float(Temp[2])+Volt_offset,(float(Temp[3])*current_scale)/electrode_area])

	#get output file name from input file name
	oname=F[:-4]
	#print(oname)

	#cast output data array as a numpy array
	Odata=np.asarray(Odata)
 	#print(Odata)

	#Do math if you want
	#temp=Odata[0:10,1]
	#print(temp)
	#print(np.average(temp))
	
	#save output
	np.savetxt(wd+oname+'_xy.txt',Odata, header='#'+oname+'_V, #'+oname+'_i')

	

