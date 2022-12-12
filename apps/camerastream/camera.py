from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from os.path import dirname, join

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()


# class IPWebCam(object):
# 	def __init__(self, camera):
# 		self.url =f"http://{camera.ip}:{camera.port}/shot.jpg"

# 	def __del__(self):
# 		cv2.destroyAllWindows()

# 	def get_frame(self):
# 		imgResp = urllib.request.urlopen(self.url)
# 		imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
# 		img= cv2.imdecode(imgNp,-1)
# 		frame_flip = cv2.flip(img,1)
# 		ret, jpeg = cv2.imencode('.jpg', frame_flip)
# 		return jpeg.tobytes()

class LiveWebCam(object):
	def __init__(self, camera): 
		if camera.login != '' or camera.password != '':
			self.url = cv2.VideoCapture(f'rtsp://{camera.ip}:{camera.port}//user={camera.login}_password={camera.password}_channel=1_stream=0.sdp?real_stream') 
		else:
			self.url = cv2.VideoCapture(f'rtsp://{camera.ip}:{camera.port}/h264_ulaw.sdp')
		

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()



