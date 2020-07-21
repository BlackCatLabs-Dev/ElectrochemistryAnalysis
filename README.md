# ElectrochemistryAnalysis
Allows the extraction and basic computations for electrocatalysis data

The files contained here are for basic processing of electrochemistry data. This data is generated from Gamery framework. You may have to modify if you use a diffrent system. I try and point out lines that may be modified below.

# rawLSV_to_txtLSV
Command line: python3 rawLSV_to_txtLSV.py wd voltOffset current_scale electrodeArea
wd= where are the files to operate on
voltOffset = how much to add to every voltage, if you do not want to change from the refrence electrode to a standard, put 0 
current_scale = current is output as Amps, 1000 changes to mA. Put 1 to avoid mutliplication 
electrodeArea = what is the electrode area?
The output will be a two columb file with voltage in 0 and current denisty (current/area) in 1. 

Possible Changes:
Line 38 if Temp[0]=='#': 
#/ occures right before data starts, put your own flag as needed 

# CP_converter
For converting cronopotental scans into voltage over time
Command Line: python3 CP_converter.py wd nameOfFileToSave.txt 

# ratevscurrent 
For producing a plot of the scan rate vs current for electrochemical surface area determination. Scan rate will be in 0, current in 1. Run this on all files in a directory 
