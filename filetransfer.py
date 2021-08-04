import pytesseract
import re
import PIL.Image
import PIL.ImageDraw
from PIL import *
#from PIL import ImageEnhance
#from PIL import 
import shutil
#import cv2
import os
#import glob
#print ('Hello World')
#filepath = [f or f in glob.glob(directory + '*.jpg')]
## depends on machoing to set up folder route 
filepath = './pic'
filepath2 = './pic2'
filepath3 = './pic3'

## files stauts (how many file in the folder )
for files in os.walk(filepath):
    if len(files) != 0:
        file_tag = len(files)
        print('----------------',len(files),'files','----------------')

try:
	for file in os.listdir(filepath):
		img = Image.open(filepath+'/'+file)
		img = img.convert('L') ## change img to gray 
		## binary img into black and white 
		## threshold could define by user 
		threshold = 200
		table = []
		for i in range(256):
			if i < threshold:
				table.append(0)
			else:
				table.append(1)
		img = img.point(table,'1')
		## pytesseract detect the sheet no. automatically 
		text = pytesseract.image_to_string(img,lang='chi_tra+eng')
		## regex 
		sheetNo = re.compile(r'\d\d-\d\d\d\d\d\d\d\d-\d\d\d')
		result = sheetNo.findall(text)
		results= str(result).join(result)
		#os.replace(r'./pic/'f"{file}", r'./pic/'f"{results}")
		if len(results)!=15:
			print(filepath+'/'+f"{file}"+ " " +'was moved to another folder')
			shutil.move(filepath+'/'+file, filepath2+'/'+file)
			img.close()
			continue
		else:
			#img.save('./pic3/'f"{results}.jpg")
			shutil.move(filepath+'/'+file, './pic3/'f"{results}.jpg")
			img.close()
			print(filepath+'/'+results)
except:
	print('interrupt automatically')

#