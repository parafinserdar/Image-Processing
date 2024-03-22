import cv2

path = input("Please enter the image path : ")
img = cv2.imread(path)




gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default (1).xml')




faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)


for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)

