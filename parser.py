import re
import shutil
import os
import numpy as np 
import pandas as pd 
import datetime
import pymysql


#con = pymysql.connect(host='172.17.11.76', user='root', password="", database='')
#cur = con.cursor()


pat1 = re.compile(r'\d\d-\d\d\d\d\d\d\d\d-\d\d\d.jpg')
pat2 = re.compile(r'\d+:|blank|others')
pat3 = re.compile(r'\d+%')


print ('******************************---start---*****************************')
print (datetime.datetime.now())
filepath = './result/'
filepath2 = './result2/'

## files stauts (how many file in the folder )
for files in os.walk(filepath):
    if len(files) != 0:
        file_tag = len(files)
        print('----------------',len(files),'files','----------------')

## read files
try:
	for file in os.listdir(filepath):
		with open(filepath+'/'+ file, 'r') as txt:
			txt = txt.read()
		## mapping txt and regEx
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
				#deliverSheet_lst = [datetime.datetime.now() + listresult]
				#sql_deliverSheet_lst = "insert into deliverSheet_table values  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
				#cur.executemany(sql_deliverSheet_lst,deliverSheet_lst)
				#con.commit()
				print('OK!!!')
				print (listresult)
				print ('===================================================================================')


except:
	print('interrupt automatically')


	

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
