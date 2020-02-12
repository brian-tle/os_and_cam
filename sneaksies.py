import cv2
import os

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
	camera = cv2.VideoCapture(0)

	for pic_num in range(5):
		pic_num += 1
		return_value,image = camera.read()
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		cv2.imshow('image', gray)
		cv2.waitKey(3000)

		key = hash('youre_a_dummy')

		try:
			cv2.imwrite(path_name + '/' + str(key) + '_' + str(pic_num) + '.jpg', image)
		except:
			print("creation error")

	camera.release()
	cv2.destroyAllWindows()

CreateDirectory()
TakePictures()
