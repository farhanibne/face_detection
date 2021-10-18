import cv2
import sys


imaheapath = sys.argv[0]
cascpath = "...xml"
facecascade = cv2.CascadeClassifier(cascpath)
image = cv2.imread(imaheapath)
grey = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)
faces = facecascade.defaultMultiScale(grey,
                                      ScaleFactor=1.1,
                                      MinNeighbour=5,
                                      Minsize=(30,30),
                                      flags=cv2.cv.CV_HAAR_SCALE_IMAGE)


print("found {0} faces".format(len(faces)) )
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,0),2)

cv2.imshow("faces found",image)
cv2.waitKey(0)