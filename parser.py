import re
import shutil
import os
import numpy as np 
import pandas as pd 
import datetime

filepath = './result/'
filepath2 = './result2/'

## read txt
for file in os.listdir(filepath):
	txt = open(filepath+'/'+ file, 'r')
	txt = txt.read()
	#pat1 = re.compile(r'\d.jpg')
	pat1 = re.compile(r'\d\d-\d\d\d\d\d\d\d\d-\d\d\d.jpg')
	pat2 = re.compile(r'\d+:|blank|others')
	pat3 = re.compile(r'\d+%')
	#pat2 = re.compile(r'\n')
	result = pat1.findall(txt)
	testresult = pat2.findall(txt)
	## get each element of list and replace ':' 
	testresult = list(map(lambda x:x.replace(":",''),testresult))
	perresult = pat3.findall(txt)


	listresult = result+testresult
	
	if len(result)!=15 & len(testresult)!= 12:
		print (filepath+'/'+f"{file}" + " " + 'wrong format of file and need to check artificially ')
		print (listresult)
		print (perresult)
		print ('===================================================================================')
		shutil.move(filepath+'/'+file, filepath2+'/'+file)
		continue
	else:
		#listresult = result+testresult
		print('OK!!!')
		print (listresult)
		print ('===================================================================================')


	

	#print(result)
	#print(testresult)
	
#txt.close()
#filename = re.compile(r'/d+.jpg')
#test = filename.findall(txt)
#print (test)


#		print (results)


'''path = './pic/1.txt'
f = open(path,'w')
f.write(text)
f.close()
print(text)'''
