import cv2

#load the pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect the faces coose the image of ur choice
img = cv2.imread('multiple.jpg')


#convert the image to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#print(face_coordinates)
#draw rectangle 
i = len(face_coordinates)
print(face_coordinates)
for j in range(i):
	(x,y,w,h) = face_coordinates[j]
	cv2.rectangle(img,(x,y),(x+w ,y+h),(0,255,0),2)

#open the image 
cv2.imshow('Face Detector',img)
cv2.waitKey()

print("code completed")