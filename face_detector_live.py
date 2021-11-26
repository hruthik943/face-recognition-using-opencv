import cv2

#create classifier
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#live webcam capture
webcam = cv2.VideoCapture(0)

while True:

	#raec the current frame
	successful_frame_read, frame = webcam.read()

	#must convert to grayscale
	grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	#detect faces
	face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
	
	#draw rectangle
	i = len(face_coordinates)
	for j in range(i):
		(x,y,w,h) = face_coordinates[j]
		cv2.rectangle(frame ,(x,y),(x+w ,y+h),(0,255,0),2)

	cv2.imshow('face detector',frame)
	key = cv2.waitKey(1)

	if key==81 or key==113:
	 	break
webcam.release()
